import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(
    BASE_DIR,
    "database",
    "studyspace.db"
)


# DATABASE CONNECTION
def get_db():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    conn.execute("PRAGMA foreign_keys = ON")

    return conn


# CREATE DATABASE TABLES
def initialize_database():

    conn = get_db()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS buildings (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT UNIQUE NOT NULL

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS spaces (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        building_id INTEGER NOT NULL,

        room_type TEXT NOT NULL,

        capacity INTEGER NOT NULL CHECK(capacity > 0),

        facilities TEXT,

        FOREIGN KEY(building_id)
        REFERENCES buildings(id)

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        space_id INTEGER NOT NULL,

        student_name TEXT NOT NULL,

        booking_date TEXT NOT NULL,

        start_time TEXT NOT NULL,

        end_time TEXT NOT NULL,

        purpose TEXT NOT NULL,

        status TEXT DEFAULT 'Confirmed',

        CHECK(end_time > start_time),

        FOREIGN KEY(space_id)
        REFERENCES spaces(id)

    )
    """)

    # INSERT SAMPLE BUILDINGS
    if cursor.execute(
        "SELECT COUNT(*) FROM buildings"
    ).fetchone()[0] == 0:

        cursor.executemany(
            "INSERT INTO buildings(name) VALUES (?)",
            [
                ("Academic Block A",),
                ("Library Block",)
            ]
        )

    # INSERT SAMPLE SPACES
    if cursor.execute(
        "SELECT COUNT(*) FROM spaces"
    ).fetchone()[0] == 0:

        cursor.executemany("""
        INSERT INTO spaces
        (name, building_id, room_type, capacity, facilities)

        VALUES (?, ?, ?, ?, ?)

        """, [

            ("Discussion Room A1", 1, "Discussion Room", 8,
             "Wi-Fi, Whiteboard"),

            ("Project Lab A2", 1, "Project Room", 20,
             "Computers, Projector"),

            ("Reading Room B1", 2, "Study Room", 30,
             "Wi-Fi, Charging"),

            ("Seminar Hall B2", 2, "Seminar Hall", 60,
             "Projector, Audio")

        ])

    conn.commit()

    conn.close()