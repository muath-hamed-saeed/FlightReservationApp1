# reservations.py
import tkinter as tk
from tkinter import ttk, messagebox
from database import get_reservations, delete_reservation

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ffffff")
        self.controller = controller

        title = tk.Label(self, text="All Reservations", font=("Segoe UI", 16, "bold"), bg="#ffffff")
        title.pack(pady=(20, 5))

        controls = tk.Frame(self, bg="#ffffff")
        controls.pack(pady=5)

        tk.Button(controls, text="Refresh", width=12, command=self.refresh).grid(row=0, column=0, padx=4)
        tk.Button(controls, text="New Booking", width=12, command=lambda: controller.show_frame("BookingPage")).grid(row=0, column=1, padx=4)
        tk.Button(controls, text="Edit Selected", width=12, command=self.edit_selected).grid(row=0, column=2, padx=4)
        tk.Button(controls, text="Delete Selected", width=12, command=self.delete_selected).grid(row=0, column=3, padx=4)
        tk.Button(controls, text="Back to Home", width=12, command=lambda: controller.show_frame("HomePage")).grid(row=0, column=4, padx=4)

        columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
            width = 100
            if col == "id": width = 40
            if col in ("name", "destination", "departure"): width = 130
            self.tree.column(col, width=width, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=12, pady=10)

    def on_show(self, **kwargs):
        self.refresh()

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in get_reservations():
            self.tree.insert("", "end", values=row)

    def _get_selected_id(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("No Selection", "Please select a reservation from the table first.")
            return None
        return int(self.tree.item(sel[0])["values"][0])

    def edit_selected(self):
        res_id = self._get_selected_id()
        if res_id is not None:
            self.controller.set_edit_reservation(res_id)

    def delete_selected(self):
        res_id = self._get_selected_id()
        if res_id is not None:
            if self.controller.confirm("Confirm Delete", "Are you sure you want to delete this reservation?"):
                delete_reservation(res_id)
                self.refresh()
                messagebox.showinfo("Deleted", "The reservation has been deleted.")
