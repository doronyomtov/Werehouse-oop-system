import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class ChartView:

    def __init__(self, manage, root, start_row):
        self.manage = manage
        self.root = root
        self.start_row = start_row
        self.selected_item = 'Choose Stats'
        self.canvas = None

    def show(self):
        self.create_combobox()
        self.create_lbl()
        self.create_chart()

    def create_combobox(self):
        self.filter_combobox_var = tk.StringVar()
        filter_values = ['Choose Stats', 'Quantity By Location', 'Employee By Phone', 'Employee By Gender']
        chart_combobox = ttk.Combobox(
            self.root,
            values=filter_values,
            textvariable=self.filter_combobox_var,
            state='readonly',
            width=25,
            font=('Arial', 10),
            foreground='black',
            background='white',
            justify='center')
        chart_combobox.grid(column=1, row=11)
        chart_combobox.current(0)
        chart_combobox.bind("<<ComboboxSelected>>", lambda event: self.combobox_choosen(chart_combobox))

    def create_lbl(self):
        statistic_lbl = tk.Label(
            self.root,
            text="Statistics",
            font=("Arial", 14),
            fg="blue")
        statistic_lbl.grid(column=0, row=10)

        choose_stats_lbl = tk.Label(
            self.root,
            text="Chose stats",
            font=("Arial", 10),
            fg="blue")
        choose_stats_lbl.grid(column=0, row=11)

    def combobox_choosen(self, combobox):
        self.selected_item = combobox.get()
        self.create_chart()

    def create_chart(self):
        if self.selected_item == 'Quantity By Location':
            x = self.manage.warehouse.get_all_location()
            y = list(self.manage.warehouse.get_location_total_quantity().values())
            fig = Figure(figsize=(6, 3), dpi=100)
            ax = fig.add_subplot(111)
            ax.bar(x, y)
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=12, columnspan=3)
            self.canvas = canvas
        if self.selected_item == 'Employee By Phone':
            x =['050','052','053','054','056']
            y =[0,0,0,0,0]
            for i in self.manage.employee:
                if i.phone_number[0:3] == '050':
                    y[0] +=1
                if i.phone_number[0:3] == '052':
                    y[1] +=1
                if i.phone_number[0:3] == '053':
                    y[2] +=1
                if i.phone_number[0:3] == '054':
                    y[3] +=1
                if i.phone_number[0:3] == '056':
                    y[4] +=1
            fig = Figure(figsize=(6, 3), dpi=100)
            ax = fig.add_subplot(111)
            ax.bar(x, y)
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=12, columnspan=3)
            self.canvas =canvas
        if self.selected_item == 'Employee By Gender':
            x = ['M', 'F']
            y = [0, 0]
            for i in self.manage.employee:
                if i.gender == 'M':
                    y[0] += 1
                else:
                    y[1] += 1
            fig = Figure(figsize=(6, 3), dpi=100)
            ax = fig.add_subplot(111)
            ax.bar(x, y)
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=12, columnspan=3)
            self.canvas = canvas
        if self.selected_item == 'Choose Stats' and self.canvas is not None:
            self.canvas.get_tk_widget().destroy()
