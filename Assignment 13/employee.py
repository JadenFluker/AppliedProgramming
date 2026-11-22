def check_text(value, label):
    "makes sure the value is a string, the setters use this"
    if type(value)!=str:
        raise TypeError(label + " must be a string")


class Employee:
    "an employee with a name, id number, department and position"

    def __init__(self, name="", id_number=0, department="", position=""):
        "all four values, or just the name and id number, or nothing at all (empty strings and 0)"
        self.set_name(name)
        self.set_id_number(id_number)
        self.set_department(department)
        self.set_position(position)

    def get_name(self):
        "returns the name"
        return self.__name

    def set_name(self, name):
        "sets the name, has to be a string"
        check_text(name, "name")
        self.__name = name

    def get_id_number(self):
        "returns the id number"
        return self.__id_number

    def set_id_number(self, id_number):
        "sets the id number, has to be a whole number that is 0 or more"
        if type(id_number)!=int:
            raise TypeError("id number must be a whole number")
        if id_number<0:
            raise ValueError("id number cant be negative")
        self.__id_number = id_number

    def get_department(self):
        "returns the department"
        return self.__department

    def set_department(self, department):
        "sets the department, has to be a string"
        check_text(department, "department")
        self.__department = department

    def get_position(self):
        "returns the position"
        return self.__position

    def set_position(self, position):
        "sets the position, has to be a string"
        check_text(position, "position")
        self.__position = position
