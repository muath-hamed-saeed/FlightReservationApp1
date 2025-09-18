# main.py
import tkinter as tk
from tkinter import messagebox
from database import init_db
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation App")
        self.geometry("820x520")
        self.resizable(False, False)

        # Initialize DB
        init_db()

        # Container for pages
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Shared state
        self._state = {
            "edit_reservation_id": None
        }

        # Instantiate pages
        self.frames = {}
        for PageClass in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name, **kwargs):
        frame = self.frames[page_name]
        if hasattr(frame, "on_show"):
            frame.on_show(**kwargs)
        frame.tkraise()

    def set_edit_reservation(self, reservation_id: int):
        self._state["edit_reservation_id"] = reservation_id
        self.show_frame("EditReservationPage")

    def get_edit_reservation(self):
        return self._state.get("edit_reservation_id")

    def confirm(self, title, message):
        return messagebox.askyesno(title, message)

if __name__ == "__main__":
    app = App()
    app.mainloop()
