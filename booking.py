# booking.py
import tkinter as tk
from tkinter import messagebox
from database import create_reservation

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ffffff")
        self.controller = controller

        title = tk.Label(self, text="Book a Flight", font=("Segoe UI", 16, "bold"), bg="#ffffff")
        title.pack(pady=(20, 10))

        form = tk.Frame(self, bg="#ffffff")
        form.pack(pady=10)

        self.entries = {}
        fields = [
            ("Name", "name"),
            ("Flight Number", "flight_number"),
            ("Departure", "departure"),
            ("Destination", "destination"),
            ("Date (YYYY-MM-DD)", "date"),
            ("Seat Number", "seat_number"),
        ]

        for i, (label, key) in enumerate(fields):
            tk.Label(form, text=label, anchor="w", width=18, bg="#ffffff").grid(row=i, column=0, padx=5, pady=6, sticky="w")
            entry = tk.Entry(form, width=40)
            entry.grid(row=i, column=1, padx=5, pady=6)
            self.entries[key] = entry

        btns = tk.Frame(self, bg="#ffffff")
        btns.pack(pady=15)

        tk.Button(btns, text="Save", width=14, command=self.save).grid(row=0, column=0, padx=5)
        tk.Button(btns, text="Back", width=14, command=lambda: self.controller.show_frame("HomePage")).grid(row=0, column=1, padx=5)

    def on_show(self, **kwargs):
        for e in self.entries.values():
            e.delete(0, tk.END)

    def save(self):
        data = {k: e.get().strip() for k, e in self.entries.items()}
        if any(not v for v in data.values()):
            messagebox.showerror("Validation error", "Please fill all fields.")
            return

        try:
            create_reservation(**data)
            messagebox.showinfo("Success", "Reservation created successfully.")
            self.controller.show_frame("ReservationsPage")
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to save reservation.\n{ex}")
