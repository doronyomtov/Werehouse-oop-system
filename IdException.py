import tkinter as tk


class IdException(BaseException):
    def __init__(self, frame, id):
        self.frame = frame
        self.id = id

    def __str__(self):
        fail_id_lbl = tk.Label(
            self.frame,
            text=f'id {self.id} is not correct',
            font=("Arial", 12),
            fg="red",
            width=50, )
        fail_id_lbl.grid(column=0, row=0, columnspan=4)
