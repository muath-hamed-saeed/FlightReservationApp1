
---

# ✈️ Flight Reservation App – Tkinter + SQLite

**Flight Reservation App** is a simple and user-friendly desktop application for booking airline tickets, developed in **Python** using **Tkinter** for the graphical user interface and **SQLite** for database management.  
The app provides a multi-page interface to add, view, update, and delete reservations with ease, and can be run directly from the source code or as a standalone executable (.exe).

---

## 🚀 Features
- **Create Reservations**: Enter passenger details, flight number, departure, destination, travel date, and seat number.
- **View Reservations**: Display all bookings in a clear, tabular format.
- **Update Reservations**: Edit any details of an existing booking.
- **Delete Reservations**: Remove unwanted bookings from the database.
- **Multi-Page Interface**: Smooth navigation between booking, viewing, and editing pages.
- **Local Database**: Store data using SQLite without requiring an internet connection.

---

## 🛠️ Requirements
- Python 3.x
- Libraries listed in `requirements.txt`
- *(Optional)* PyInstaller if you want to build the executable

---

## 📂 Project Structure
```
FlightReservationApp/
│-- main.py               # Main application file
│-- database.py           # SQLite database connection
│-- home.py               # Home page UI
│-- booking.py            # Flight booking form
│-- reservations.py       # View all reservations
│-- edit_reservation.py   # Update/Delete functionality
│-- flights.db            # SQLite database file
│-- requirements.txt      # Required Python libraries
│-- README.md             # Project documentation
│-- dist/                  # Contains the final executable file
```

---

## ▶️ How to Run

### 1. From Source Code:
```bash
pip install -r requirements.txt
python main.py
```

### 2. From Executable:
- Open the `dist/` folder.
- Run `FlightReservationApp.exe` directly.

---

## 📸 Screenshots
*(Add screenshots of your application interface here)*

---

## 📜 License
This project is available for educational and personal use.

---
