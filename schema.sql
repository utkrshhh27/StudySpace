CREATE TABLE buildings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE spaces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    building_id INTEGER NOT NULL,
    room_type TEXT NOT NULL,
    capacity INTEGER NOT NULL CHECK(capacity > 0),
    facilities TEXT,
    FOREIGN KEY(building_id) REFERENCES buildings(id)
);

CREATE TABLE bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    space_id INTEGER NOT NULL,
    student_name TEXT NOT NULL,
    booking_date TEXT NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    purpose TEXT NOT NULL,
    status TEXT DEFAULT 'Confirmed',
    CHECK(end_time > start_time),
    FOREIGN KEY(space_id) REFERENCES spaces(id)
);