import tkinter as tk


class PhoneNumberException(BaseException):
    def __init__(self, frame):
        self.frame = frame

    def __str__(self):
        fail_lbl = tk.Label(
            self.frame,
            text=f"Phone number is wrong",
            font=("Arial", 12),
            fg="red",
            width=50, )
        fail_lbl.grid(column=0, row=0, columnspan=4)
