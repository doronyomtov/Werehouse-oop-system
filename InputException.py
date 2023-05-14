import tkinter as tk


class InputException(BaseException):
    def __init__(self, msg, frame):
        self.msg = msg
        self.frame = frame
        super().__init__(msg)

    def __str__(self):
        fail_lbl = tk.Label(
            self.frame,
            text=f"{self.msg}",
            font=("Arial", 12),
            fg="red",
            width=50, )
        fail_lbl.grid(column=0, row=0 ,columnspan=4)
