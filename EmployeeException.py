import tkinter as tk


class EmployeeException(BaseException):
    def __init__(self, frame, id):
        self.frame = frame
        self.id = id

    def __str__(self):
        fail_lbl = tk.Label(
            self.frame,
            text=f"employee with the id {self.id} is already registered",
            font=("Arial", 12),
            fg="red",
            width=50, )
        fail_lbl.grid(column=0, row=0 ,columnspan=4)
