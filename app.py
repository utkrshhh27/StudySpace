import os
import sys

from flask import Flask, render_template, request, redirect, url_for, flash

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from database.db import get_db, initialize_database

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "frontend"),
    static_folder=os.path.join(BASE_DIR, "frontend"),
    static_url_path="/static"
)

app.secret_key = "studyspace-demo-key"


@app.route("/")
def home():
    conn = get_db()

    building = request.args.get("building", "")
    room_type = request.args.get("type", "")

    query = """
    SELECT spaces.*, buildings.name AS building_name
    FROM spaces
    JOIN buildings ON spaces.building_id = buildings.id
    WHERE 1=1
    """

    values = []

    if building:
        query += " AND buildings.id = ?"
        values.append(building)

    if room_type:
        query += " AND spaces.room_type = ?"
        values.append(room_type)

    spaces = conn.execute(query, values).fetchall()
    buildings = conn.execute("SELECT * FROM buildings").fetchall()
    types = conn.execute(
        "SELECT DISTINCT room_type FROM spaces"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        spaces=spaces,
        buildings=buildings,
        types=types
    )


@app.route("/book/<int:space_id>", methods=["POST"])
def book(space_id):
    name = request.form.get("student_name", "").strip()
    date = request.form.get("booking_date", "")
    start = request.form.get("start_time", "")
    end = request.form.get("end_time", "")
    purpose = request.form.get("purpose", "").strip()

    if not all([name, date, start, end, purpose]) or end <= start:
        flash("Please enter valid booking details.", "error")
        return redirect(url_for("home"))

    conn = get_db()

    space = conn.execute(
        "SELECT id FROM spaces WHERE id = ?", (space_id,)
    ).fetchone()

    if not space:
        conn.close()
        flash("Room not found.", "error")
        return redirect(url_for("home"))

    conflict = conn.execute("""
        SELECT id FROM bookings
        WHERE space_id = ?
        AND booking_date = ?
        AND status = 'Confirmed'
        AND start_time < ?
        AND end_time > ?
    """, (space_id, date, end, start)).fetchone()

    if conflict:
        flash("This room is already booked at that time.", "error")
    else:
        conn.execute("""
            INSERT INTO bookings
            (space_id, student_name, booking_date,
             start_time, end_time, purpose)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (space_id, name, date, start, end, purpose))

        conn.commit()
        flash("Booking successful!", "success")

    conn.close()
    return redirect(url_for("home"))


@app.route("/bookings")
def bookings():
    conn = get_db()

    records = conn.execute("""
        SELECT bookings.*,
        spaces.name AS space_name,
        buildings.name AS building_name
        FROM bookings
        JOIN spaces ON bookings.space_id = spaces.id
        JOIN buildings ON spaces.building_id = buildings.id
        ORDER BY booking_date DESC, start_time DESC
    """).fetchall()

    conn.close()

    return render_template("bookings.html", bookings=records)


@app.route("/cancel/<int:booking_id>", methods=["POST"])
def cancel(booking_id):
    conn = get_db()

    conn.execute("""
        UPDATE bookings
        SET status = 'Cancelled'
        WHERE id = ?
    """, (booking_id,))

    conn.commit()
    conn.close()

    flash("Booking cancelled successfully!", "success")
    return redirect(url_for("bookings"))


@app.route("/add_space", methods=["GET", "POST"])
def add_space():
    conn = get_db()

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        building_id = request.form.get("building_id", "")
        room_type = request.form.get("room_type", "")
        capacity = request.form.get("capacity", "")
        facilities = request.form.get("facilities", "").strip()
        
        try:
            capacity = int(capacity)

            if not name or not building_id or not room_type or capacity <= 0:
                raise ValueError()

            conn.execute("""
                INSERT INTO spaces
                (name, building_id, room_type, capacity, facilities)
                VALUES (?, ?, ?, ?, ?)
            """, (name, building_id, room_type, capacity, facilities))

            conn.commit()
            conn.close()

            flash("New space added successfully!", "success")
            return redirect(url_for("home"))

        except ValueError:
            flash("Please enter valid space details.", "error")

    buildings = conn.execute(
        "SELECT * FROM buildings"
    ).fetchall()

    conn.close()

    return render_template("add_space.html", buildings=buildings)


@app.route("/health")
def health():
    return {"status": "running", "project": "StudySpace"}


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)