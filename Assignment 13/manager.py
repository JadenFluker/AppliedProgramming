from employee import Employee


class Manager(Employee):
    "a manager is an employee that also has a salary"

    def __init__(self, name="", id_number=0, department="", position="", salary=0):
        "same as employee plus a salary, all of them are optional"
        Employee.__init__(self, name, id_number, department, position)
        self.set_salary(salary)

    def get_salary(self):
        "returns the salary"
        return self.__salary

    def set_salary(self, salary):
        "sets the salary, has to be a number that is 0 or more"
        if type(salary)!=int and type(salary)!=float:
            raise TypeError("salary must be a number")
        if salary<0:
            raise ValueError("salary cant be negative")
        self.__salary = float(salary)

    def give_raise(self, percent):
        "raises the salary by a percent, 10 means 10 percent"
        if type(percent)!=int and type(percent)!=float:
            raise TypeError("raise percent must be a number")
        if percent<0:
            raise ValueError("raise percent cant be negative")
        self.__salary = round(self.__salary + self.__salary * percent / 100, 2)

    def get_position(self):
        "overrides the employee version, puts Manager in front of the position"
        position = Employee.get_position(self)
        if position=="":
            return "Manager"
        return "Manager - " + position
