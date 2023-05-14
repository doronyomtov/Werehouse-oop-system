from Person import Person
from data_utilis import validate_gender, validate_number


class Employee(Person):
    def __init__(self, e_id, firstname, lastname, address, phone_number, gender):
        super().__init__(e_id, firstname, lastname)
        self.address = address
        self.phone_number = phone_number if validate_number(phone_number) == True else None
        self.gender = validate_gender(gender)
        self.email = f'{firstname}.{lastname}@email.com'

    def __str__(self):
        return f'{super().__str__()},{self.email},{self.address},{self.phone_number},{self.gender}'

    def __repr__(self):
        return self.__str__()