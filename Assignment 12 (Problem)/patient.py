def check_text(value, label):
    "makes sure the value is a string, the setters use this"
    if type(value)!=str:
        raise TypeError(label + " must be a string")


class Patient:
    "a patient with a name, address, phone number and an emergency contact"

    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone, emergency_name, emergency_phone):
        "takes a value for every member variable, each one goes through its setter so it gets checked"
        self.set_first_name(first_name)
        self.set_middle_name(middle_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_city(city)
        self.set_state(state)
        self.set_zip_code(zip_code)
        self.set_phone(phone)
        self.set_emergency_name(emergency_name)
        self.set_emergency_phone(emergency_phone)

    def get_first_name(self):
        "returns the first name"
        return self.__first_name

    def set_first_name(self, first_name):
        "sets the first name, has to be a string"
        check_text(first_name, "first name")
        self.__first_name = first_name

    def get_middle_name(self):
        "returns the middle name"
        return self.__middle_name

    def set_middle_name(self, middle_name):
        "sets the middle name, has to be a string"
        check_text(middle_name, "middle name")
        self.__middle_name = middle_name

    def get_last_name(self):
        "returns the last name"
        return self.__last_name

    def set_last_name(self, last_name):
        "sets the last name, has to be a string"
        check_text(last_name, "last name")
        self.__last_name = last_name

    def get_address(self):
        "returns the address"
        return self.__address

    def set_address(self, address):
        "sets the address, has to be a string"
        check_text(address, "address")
        self.__address = address

    def get_city(self):
        "returns the city"
        return self.__city

    def set_city(self, city):
        "sets the city, has to be a string"
        check_text(city, "city")
        self.__city = city

    def get_state(self):
        "returns the state"
        return self.__state

    def set_state(self, state):
        "sets the state, has to be a string"
        check_text(state, "state")
        self.__state = state

    def get_zip_code(self):
        "returns the zip code"
        return self.__zip_code

    def set_zip_code(self, zip_code):
        "sets the zip code, has to be a string"
        check_text(zip_code, "zip code")
        self.__zip_code = zip_code

    def get_phone(self):
        "returns the phone number"
        return self.__phone

    def set_phone(self, phone):
        "sets the phone number, has to be a string"
        check_text(phone, "phone number")
        self.__phone = phone

    def get_emergency_name(self):
        "returns the name of the emergency contact"
        return self.__emergency_name

    def set_emergency_name(self, emergency_name):
        "sets the name of the emergency contact, has to be a string"
        check_text(emergency_name, "emergency contact name")
        self.__emergency_name = emergency_name

    def get_emergency_phone(self):
        "returns the phone number of the emergency contact"
        return self.__emergency_phone

    def set_emergency_phone(self, emergency_phone):
        "sets the phone number of the emergency contact, has to be a string"
        check_text(emergency_phone, "emergency contact phone number")
        self.__emergency_phone = emergency_phone
