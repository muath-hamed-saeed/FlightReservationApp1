# edit_reservation.py
import tkinter as tk
from tkinter import messagebox
from database import get_reservation, update_reservation

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ffffff")
        self.controller = controller
        self.current_id = None

        title = tk.Label(self, text="Edit Reservation", font=("Segoe UI", 16, "bold"), bg="#ffffff")
        title.pack(pady=(20, 10))

        form = tk.Frame(self, bg="#ffffff")
        form.pack(pady=10)

        self.entries = {}
        fields = [
            ("Name", "name"), ("Flight Number", "flight_number"), ("Departure", "departure"),
            ("Destination", "destination"), ("Date (YYYY-MM-DD)", "date"), ("Seat Number", "seat_number"),
        ]

        for i, (label, key) in enumerate(fields):
            tk.Label(form, text=label, anchor="w", width=18, bg="#ffffff").grid(row=i, column=0, padx=5, pady=6, sticky="w")
            entry = tk.Entry(form, width=40)
            entry.grid(row=i, column=1, padx=5, pady=6)
            self.entries[key] = entry

        btns = tk.Frame(self, bg="#ffffff")
        btns.pack(pady=15)

        tk.Button(btns, text="Update", width=14, command=self.update).grid(row=0, column=0, padx=5)
        tk.Button(btns, text="Back", width=14, command=lambda: self.controller.show_frame("ReservationsPage")).grid(row=0, column=1, padx=5)

    def on_show(self, **kwargs):
        self.current_id = self.controller.get_edit_reservation()
        if self.current_id is None:
            self.controller.show_frame("ReservationsPage")
            return

        res = get_reservation(self.current_id)
        if not res:
            messagebox.showerror("Not Found", "Reservation not found.")
            self.controller.show_frame("ReservationsPage")
            return

        # Unpack tuple: id, name, flight_number, ...
        _, name, flight_number, departure, destination, date, seat_number = res
        data = {
            "name": name, "flight_number": flight_number, "departure": departure,
            "destination": destination, "date": date, "seat_number": seat_number
        }
        for key, value in data.items():
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, value)

    def update(self):
        if self.current_id is None: return

        data = {k: e.get().strip() for k, e in self.entries.items()}
        if any(not v for v in data.values()):
            messagebox.showerror("Validation Error", "Please fill all fields.")
            return

        try:
            update_reservation(self.current_id, **data)
            messagebox.showinfo("Updated", "Reservation updated successfully.")
            self.controller.show_frame("ReservationsPage")
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to update reservation.\n{ex}")
