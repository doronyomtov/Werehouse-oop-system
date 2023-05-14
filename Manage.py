from Employee import Employee
from Manager import Manager
from Warehouse import Warehouse


class Manage:
    def __init__(self, warehouse, employee=[], managers={}):
        self.warehouse = Warehouse()
        self.employee = employee
        self.managers = managers

    def __str__(self):
        return f'Manage class - Python OOP course - assignment'

    def __repr__(self):
        return f'Manage class - Python OOP course - assignment'

    def add_product(self):
        name = input("insert product name:")
        description = input("insert product description:")
        quantity = input("insert product quantity:")
        location = input("insert product location:")
        return Warehouse.add_product(name, description, quantity, location)

    def remove_product(self):
        sku = input("insert product sku:")
        print(f'{sku} deleted') if Warehouse.remove_product(sku) is True else print("Error")

    def add_employee(self, e_id, firstname, lastname, phone_number, address, gender):
        if self.is_inside(e_id):
            print("Error")
        else:
            employee = Employee(e_id, firstname, lastname, address, phone_number, gender)
            self.employee.append(employee)
            print(f'Employee added')

    def remove_employee(self, e_id):
        was_found = False
        for i in range(len(self.employee)):
            if e_id == self.employee[i].e_id:
                self.employee.pop(i)
                was_found = True
        print(f'{e_id} deleted') if was_found is True else print("Error")

    def is_inside(self, e_id1):
        for i in self.employee:
            if isinstance(i, Employee) and i.e_id == e_id1:
                return True
        return False

    def print_products(self):
        for i in range(len(self.warehouse.products)):
            print(self.warehouse.products[i])

    def print_employee(self):
        for i in range(len(self.employee)):
            print(self.employee[i])

    def add_manager(self, e_id, firstname, lastname, address, phone_number, gender, max_employees, employees=[]):
        if not self.is_inside(e_id):
            print('error')
        else:
            manager = Manager(e_id, firstname, lastname, address, phone_number, gender, max_employees, employees)
            self.managers[e_id] = manager
            self.employee.append(manager)

    def remove_manager(self, e_id):
        if not self.is_inside(e_id):
            print('error')
        else:
            self.managers.pop(e_id)
            for i in range(len(self.employee)):
                if e_id == self.employee[i].e_id:
                    self.employee.pop(i)

    def convert_employee_to_manager(self, e_id, max_employees):
        if not self.is_inside(e_id):
            print('error')
        else:
            for i in range(len(self.employee)):
                if e_id in self.employee[i].e_id:
                    manager = Manager(e_id, self.employee[i].firstname, self.employee[i].lastname,
                                      self.employee[i].phone_number,
                                      self.employee[i].address, self.employee[i].gender, max_employees)
                    self.employee[i] = manager
                    self.managers[e_id] = manager
                    print('convert employee to be manager succeed')

    def print_employees_of_manager(self, e_id):
        self.managers[e_id].print_employees()

    def print_free_employees(self):
        occupied_employees = []
        for i in self.managers.keys():
            if len(self.managers[i].employees) > 0:
                occupied_employees.append(self.managers[i].employees)
        for j in range(len(self.employee)):
            if not [self.employee[j]] in occupied_employees:
                print(self.employee[j])

    def find_employee(self, e_id):
        for i in self.employee:
            if i.e_id == e_id:
                return i

    def get_only_employee_list(self):
        list1=[]
        for i in self.employee:
            if not isinstance(i,Manager):
                list1.append(i)

        return list1
