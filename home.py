# home.py
import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f7fafc")
        self.controller = controller

        title = tk.Label(self, text="Flight Reservation App", font=("Segoe UI", 20, "bold"), bg="#f7fafc")
        subtitle = tk.Label(self, text="Book, view, update and delete reservations", font=("Segoe UI", 12), bg="#f7fafc")

        btn_book = tk.Button(self, text="Book Flight", width=20, height=2, command=lambda: controller.show_frame("BookingPage"))
        btn_view = tk.Button(self, text="View Reservations", width=20, height=2, command=lambda: controller.show_frame("ReservationsPage"))

        title.pack(pady=(50, 10))
        subtitle.pack(pady=(0, 30))
        btn_book.pack(pady=10)
        btn_view.pack(pady=10)

    def on_show(self, **kwargs):
        pass
