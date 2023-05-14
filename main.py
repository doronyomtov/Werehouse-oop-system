from App import App
from Employee import Employee
from Manage import Manage
from Product import Product
from Warehouse import Warehouse
# from App import App
from data_utilis import read_csv_file


def get_products():
    products = read_csv_file('products_list.csv')
    products = []
    return products


def get_employees():
    employees = read_csv_file('employees_list.csv')
    return employees


def main():
    warehouse = Warehouse()
    manage = Manage(warehouse)
    products = read_csv_file('products_list.csv')
    employees = read_csv_file('employees_list.csv')
    for i in range(len(products)):
        warehouse.add_product(products[i][0], products[i][1], products[i][2],
                              products[i][3])
    for i in range(len(employees)):
        manage.add_employee(employees[i][0], employees[i][1], employees[i][2],
                            employees[i][3], employees[i][4], employees[i][5])

    managers = {
        '040436719': ['670208073', '976070029', '125931469', '880494554'],
        '529664732': ['756089454', '639372465', '666209465'],
        '524042850': ['657709986', '259542132', '623947496'],
        '557313954': ['378873020', '403402878', '285240784', '425545415']}
    # set managers
    for m, v in managers.items():
        manage.convert_employee_to_manager(m, 4)
        manager = manage.find_employee(m)
        for e in v:
            manager.add_employee(manage.find_employee(e))

    app = App(manage)
    app.show()


if __name__ == '__main__':
    main()
