def check_text(value, label):
    "makes sure the value is a string, the setters use this"
    if type(value)!=str:
        raise TypeError(label + " must be a string")


class Procedure:
    "a medical procedure done on a patient"

    def __init__(self, name, date, practitioner, charges):
        "takes a value for every member variable, each one goes through its setter so it gets checked"
        self.set_name(name)
        self.set_date(date)
        self.set_practitioner(practitioner)
        self.set_charges(charges)

    def get_name(self):
        "returns the name of the procedure"
        return self.__name

    def set_name(self, name):
        "sets the name of the procedure, has to be a string"
        check_text(name, "procedure name")
        self.__name = name

    def get_date(self):
        "returns the date of the procedure"
        return self.__date

    def set_date(self, date):
        "sets the date of the procedure, has to be a string"
        check_text(date, "date")
        self.__date = date

    def get_practitioner(self):
        "returns the practitioner who did the procedure"
        return self.__practitioner

    def set_practitioner(self, practitioner):
        "sets the practitioner, has to be a string"
        check_text(practitioner, "practitioner")
        self.__practitioner = practitioner

    def get_charges(self):
        "returns the charges"
        return self.__charges

    def set_charges(self, charges):
        "sets the charges, has to be a number that is 0 or more"
        if type(charges)!=int and type(charges)!=float:
            raise TypeError("charges must be a number")
        if charges<0:
            raise ValueError("charges cant be negative")
        self.__charges = float(charges)
