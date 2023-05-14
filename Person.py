from data_utilis import validate_id_number


class Person:
    def __init__(self, e_id, firstname, lastname):
        self.e_id = e_id if validate_id_number(e_id) == True else None
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f' {self.__class__.__name__}: {self.e_id},' \
               f'{self.firstname},{self.lastname}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.e_id == other.e_id
        else:
            return False
