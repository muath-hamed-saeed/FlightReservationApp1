# database.py
import sqlite3
from contextlib import closing

DB_NAME = "flights.db"

def _connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    with _connect() as conn, closing(conn.cursor()) as c:
        c.execute("""
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                flight_number TEXT NOT NULL,
                departure TEXT NOT NULL,
                destination TEXT NOT NULL,
                date TEXT NOT NULL,
                seat_number TEXT NOT NULL
            )
        """)
        conn.commit()

def create_reservation(name, flight_number, departure, destination, date, seat_number):
    with _connect() as conn, closing(conn.cursor()) as c:
        c.execute("""
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, flight_number, departure, destination, date, seat_number))
        conn.commit()
        return c.lastrowid

def get_reservations():
    with _connect() as conn, closing(conn.cursor()) as c:
        c.execute("SELECT id, name, flight_number, departure, destination, date, seat_number FROM reservations ORDER BY id DESC")
        return c.fetchall()

def get_reservation(reservation_id):
    with _connect() as conn, closing(conn.cursor()) as c:
        c.execute("SELECT id, name, flight_number, departure, destination, date, seat_number FROM reservations WHERE id = ?", (reservation_id,))
        return c.fetchone()

def update_reservation(reservation_id, name, flight_number, departure, destination, date, seat_number):
    with _connect() as conn, closing(conn.cursor()) as c:
        c.execute("""
            UPDATE reservations
            SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
            WHERE id = ?
        """, (name, flight_number, departure, destination, date, seat_number, reservation_id))
        conn.commit()
        return c.rowcount

def delete_reservation(reservation_id):
    with _connect() as conn, closing(conn.cursor()) as c:
        c.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
        conn.commit()
        return c.rowcount
