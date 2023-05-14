import tkinter as tk
from tkinter import ttk


class ProductsView:
    def __init__(self, root, manage, start_row):
        self.root = root
        self.manage = manage
        self.start_row = start_row
        self.filter_selected_item = 'All'
        self.length = 0

    def show(self):
        self.create_list_box()
        self.create_combobox()
        self.create_lbl()

    def filter_combobox_choosen(self, combobox):
        self.filter_selected_item = combobox.get()
        self.create_list_box()

    def create_list_box(self):

        list_box = tk.Listbox(self.root, height=self.start_row, width=80)
        list_box.grid(column=0, row=9, columnspan=3)
        if self.filter_selected_item == 'All':
            self.length = len(self.manage.warehouse.products)
            for i, products in enumerate(self.manage.warehouse.products):
                list_box.insert(i, f'{products.sku},{products.name},{products.quantity},{products.location}')
        else:
            for i, products in enumerate(self.manage.warehouse.print_product_by_location(self.filter_selected_item)):
                self.length = len(self.manage.warehouse.print_product_by_location(self.filter_selected_item))
                list_box.insert(i, products)
        self.create_lbl()
    def create_combobox(self):
        self.filter_combobox_var = tk.StringVar()
        filter_values = ['All']
        for i in self.manage.warehouse.get_all_location():
            filter_values.append(i)
        filter_combobox = ttk.Combobox(
            self.root,
            values=filter_values,
            textvariable=self.filter_combobox_var,
            state='readonly',
            width=15,
            font=('Arial', 10),
            foreground='black',
            background='white',
            justify='center'
        )
        filter_combobox.current(0)
        filter_combobox.grid(column=2, row=8)
        filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.filter_combobox_choosen(filter_combobox))

    def create_lbl(self):
        filter_lbl = tk.Label(
            self.root,
            text=f'Filter Products ({self.length})',
            font=("Arial", 12),
            fg="blue")
        filter_lbl.grid(column=0, row=8)
