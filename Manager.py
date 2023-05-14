from Employee import Employee


class Manager(Employee):

    def __init__(self, e_id, firstname, lastname, phone_number, address, gender, max_employees, employees=[]):
        super().__init__(e_id, firstname, lastname, address, phone_number, gender)
        self.max_employees = max_employees
        self.employees = employees or []

    def __str__(self):
        return f'{super().__str__()}'

    def __repr__(self):
        return self.__str__()

    def print_employees(self):
        print(f'Employeee list of manager {self.firstname},{self.lastname}:')
        for i in self.employees:
            print(i)

    def add_employee(self, employee):
        if len(self.employees) < int(self.max_employees) and isinstance(employee, Employee):
            self.employees.append(employee)
            print(f'Success')
        else:
            print(f'Failed')

    def remove_employee(self, employee):
        if isinstance(employee, Employee) and employee in self.employees:
            self.employees.remove(employee)
            print('Success')
        else:
            print("Failed")
