from employee import Employee


def show_employee(employee):
    "prints what is stored in an employee"
    print("   name:", repr(employee.get_name()))
    print("   id number:", repr(employee.get_id_number()))
    print("   department:", repr(employee.get_department()))
    print("   position:", repr(employee.get_position()))


print("Test 1: all four values in the constructor")
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
show_employee(employee1)

print("")
print("Test 2: only the name and id number in the constructor")
employee2 = Employee("Mark Jones", 39119)
show_employee(employee2)
print("   now the mutators fill in the rest")
employee2.set_department("IT")
employee2.set_position("Programmer")
show_employee(employee2)

print("")
print("Test 3: default constructor")
employee3 = Employee()
show_employee(employee3)
print("   now the mutators fill in everything")
employee3.set_name("Joy Rogers")
employee3.set_id_number(81774)
employee3.set_department("Manufacturing")
employee3.set_position("Engineer")
show_employee(employee3)


print("")
print("The three employees")
employees = [employee1, employee2, employee3]
print("Name".ljust(15), "ID Number".ljust(10), "Department".ljust(15), "Position")
print("-" * 55)
for employee in employees:
    print(employee.get_name().ljust(15), str(employee.get_id_number()).ljust(10), employee.get_department().ljust(15), employee.get_position())


print("")
print("Do they match the data from the assignment?")
expected = [
    ("Susan Meyers", 47899, "Accounting", "Vice President"),
    ("Mark Jones", 39119, "IT", "Programmer"),
    ("Joy Rogers", 81774, "Manufacturing", "Engineer")
]
for i in range(len(employees)):
    got = (employees[i].get_name(), employees[i].get_id_number(), employees[i].get_department(), employees[i].get_position())
    if got==expected[i]:
        print("   employee", i+1, "matches")
    else:
        print("   employee", i+1, "does NOT match:", got)


print("")
print("Test 4: bad values should be refused and the object should stay the same")
try:
    employee1.set_id_number("47899")
except TypeError as e:
    print("   refused:", e)

try:
    employee1.set_id_number(-5)
except ValueError as e:
    print("   refused:", e)

try:
    employee1.set_name(123)
except TypeError as e:
    print("   refused:", e)

try:
    bad_employee = Employee("Bad Data", "12")
except TypeError as e:
    print("   refused:", e)

print("   employee 1 is still", employee1.get_name(), employee1.get_id_number())
