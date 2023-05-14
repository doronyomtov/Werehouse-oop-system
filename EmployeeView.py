import tkinter as tk
from tkinter import messagebox
import numpy
from tkinter import ttk
from EmployeeException import EmployeeException
from IdException import IdException
from Employee import Employee
from InputException import InputException
from PhoneNumberException import PhoneNumberException
from data_utilis import validate_id_number,validate_number


class EmployeeView:
    def __init__(self, root, manage, start_row):
        self.root = root
        self.manage = manage
        self.start_row = int(start_row)
        self.filter_selected_item = 'All'
        self.gender_selected_item = 'M'
        self.length = 0

    def show(self):
        self.create_lebels()
        self.create_frame()
        self.create_combobox()
        self.create_list_box()

    def create_frame(self):
        frame = ttk.Frame(self.root, width=200,
                          height=20,
                          )

        frame.grid(column=0, row=3, columnspan=10)
        id_lbl = tk.Label(
            frame,
            text="Id",
            font=("Arial", 12),
            fg="blue",
        )

        id_lbl.grid(column=0, row=2)
        firstname_lbl = tk.Label(
            frame,
            text="Firstname",
            font=("Arial", 12),
            fg="blue",
            width=15)

        firstname_lbl.grid(column=1, row=2)
        lastname_lbl = tk.Label(
            frame,
            text="Lastname",
            font=("Arial", 12),
            fg="blue")

        lastname_lbl.grid(column=2, row=2)
        phone_number_lbl = tk.Label(
            frame,
            text="Phone Number",
            font=("Arial", 12),
            fg="blue",
            width=15)

        phone_number_lbl.grid(column=3, row=2)
        address_lbl = tk.Label(
            frame,
            text="Address",
            font=("Arial", 12),
            fg="blue",
            width=15, )

        address_lbl.grid(column=4, row=2)
        gender_lbl = tk.Label(
            frame,
            text="gender",
            font=("Arial", 12),
            fg="blue", )

        gender_lbl.grid(column=5, row=2)
        id_text_var = tk.StringVar()
        id_entry = tk.Entry(
            frame,
            textvariable=id_text_var,
            width=20,

            fg='black',
            bg='white',
            font=('Arial', 12),
            state='normal',
            insertbackground='red',

        )
        id_entry.grid(column=0, row=3)

        first_name_text_var = tk.StringVar()
        first_name_entry = tk.Entry(
            frame,
            textvariable=first_name_text_var,
            width=20,

            fg='black',
            bg='white',
            font=('Arial', 12),
            state='normal',
            insertbackground='red'
        )
        first_name_entry.grid(column=1, row=3)
        last_name_text_var = tk.StringVar()
        last_name_entry = tk.Entry(
            frame,
            textvariable=last_name_text_var,
            width=20,

            fg='black',
            bg='white',
            font=('Arial', 12),
            state='normal',
            insertbackground='red'
        )
        last_name_entry.grid(column=2, row=3)
        phone_number_text_var = tk.StringVar()
        phone_number_entry = tk.Entry(
            frame,
            textvariable=phone_number_text_var,
            width=20,

            fg='black',
            bg='white',
            font=('Arial', 12),
            state='normal',
            insertbackground='red'
        )
        phone_number_entry.grid(column=3, row=3)
        address_text_var = tk.StringVar()
        address_entry = tk.Entry(
            frame,
            textvariable=address_text_var,
            width=20,

            fg='black',
            bg='white',
            font=('Arial', 12),
            state='normal',
            insertbackground='red'
        )
        address_entry.grid(column=4, row=3)
        address_entry.bind()
        self.gender_combobox_var = tk.StringVar()
        gender_values = ['M', 'F']
        gender_combobox = ttk.Combobox(
            frame,
            values=gender_values,
            textvariable=self.gender_combobox_var,
            state='readonly',
            width=10,
            font=('Arial', 12),
            foreground='black',
            background='white',
            justify='center',

        )
        gender_combobox.current(0)
        gender_combobox.grid(column=5, row=3)
        gender_combobox.bind("<<ComboboxSelected>>", lambda event: self.gender_combobox_choosen(gender_combobox))

        btn = tk.Button(
            frame,
            text='Add',
            font=('Arial', 8),
            fg='black',
            width=15,
            height=1,
            command=lambda: self.add_employee(
                frame,
                id_entry.get(),
                first_name_entry.get(),
                last_name_entry.get(),
                phone_number_entry.get(),
                address_entry.get(),
                gender_combobox.get()
            )

        )
        btn.grid(column=0, row=4)

    def create_lebels(self):
        employee_lbl = tk.Label(
            self.root,
            text="Employees",
            font=("Arial", 14),
            fg="blue")

        employee_lbl.grid(column=0, row=0)

        filter_lbl = tk.Label(
            self.root,
            text=f'Filter Employees ({self.length})',
            font=("Arial", 12),
            fg="blue")
        filter_lbl.grid(row=5, column=0)

    def create_combobox(self):

        self.filter_combobox_var = tk.StringVar()
        filter_values = ['All', 'Employees', 'Managers']
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
        filter_combobox.grid(column=2, row=5)
        filter_combobox.bind("<<ComboboxSelected>>", lambda event: self.filter_combobox_choosen(filter_combobox))

    def filter_combobox_choosen(self, combobox):
        self.filter_selected_item = combobox.get()
        self.create_list_box()

    def gender_combobox_choosen(self, combobox):
        self.gender_selected_item = combobox.get()

    def create_list_box(self):
        list_box = tk.Listbox(self.root, height=self.start_row, width=80)
        list_box.grid(column=0, row=6, columnspan=3)
        if self.filter_selected_item == 'All':
            self.length = len(self.manage.employee)
            for i, employee in enumerate(self.manage.employee):
                list_box.insert(i, f'{super(Employee, employee).__str__()},{employee.phone_number}')
        if self.filter_selected_item == 'Employees':
            self.length =len(self.manage.get_only_employee_list())
            for i, employee in enumerate(self.manage.get_only_employee_list()):
                list_box.insert(i, f'{super(Employee, employee).__str__()},{employee.phone_number}')
        if self.filter_selected_item == 'Managers':
            self.length =len(list(self.manage.managers.values()))
            for i, employee in enumerate(list(self.manage.managers.values())):
                list_box.insert(i, f'{super(Employee, employee).__str__()},{employee.phone_number}')
        self.create_lebels()
        list_box.bind("<<ListboxSelect>>", self.on_list_box_select)

    def add_employee(self, frame, e_id, firstname, lastname, phone_number, address, gender):
        if e_id == '':
            raise InputException('id must not be empty', frame)
        if not validate_id_number(e_id):
            raise IdException(frame, e_id)
        if firstname == '':
            raise InputException('firstname must be not empty', frame)
        if lastname == '':
            raise InputException('lastname must be not empty', frame)
        if address == '':
            raise InputException('address must be not empty', frame)
        if phone_number == '':
            raise InputException('phone number must be not empty', frame)
        if self.manage.is_inside(e_id):
            raise EmployeeException(frame, e_id)
        if not validate_number(phone_number):
            raise PhoneNumberException(frame)
        self.manage.add_employee(e_id, firstname, lastname, phone_number, address, gender)
        messagebox.showerror('Add Employee',f'Employee {firstname} {lastname} was added')
        self.create_list_box()

    def on_list_box_select(self, event):
        list_box = event.widget
        selection = list_box.curselection()
        if len(selection) == 1:
            index = selection[0]
            if self.filter_selected_item == 'Managers':
                manager_list = list(self.manage.managers.values())
                selected_manager = manager_list[index]
                manager_employees = selected_manager.employees
                list_box = tk.Listbox(self.root, height=self.start_row, width=80)
                list_box.grid(column=5, row=6, columnspan=3)
                for i, employee in enumerate(manager_employees):
                    list_box.insert(i, f'{super(Employee, employee).__str__()},')


