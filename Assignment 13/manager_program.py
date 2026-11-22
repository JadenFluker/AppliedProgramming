from employee import Employee
from manager import Manager


def money(amount):
    "puts a dollar sign and 2 decimals on an amount"
    return "$" + format(amount, ".2f")


def show_manager(manager):
    "prints what is stored in a manager, only uses the class methods"
    print("   name:", manager.get_name())
    print("   id number:", manager.get_id_number())
    print("   department:", manager.get_department())
    print("   position:", manager.get_position())
    print("   salary:", money(manager.get_salary()))


print("Test 1: Manager with all the values in the constructor")
manager1 = Manager("Susan Meyers", 47899, "Accounting", "Vice President", 90000)
show_manager(manager1)

print("")
print("Test 2: default Manager, then the mutators add the data")
manager2 = Manager()
show_manager(manager2)
print("   now the mutators fill it in")
manager2.set_name("Mark Jones")
manager2.set_id_number(39119)
manager2.set_department("IT")
manager2.set_position("Programming Lead")
manager2.set_salary(72000)
show_manager(manager2)


print("")
print("Test 3: inheritance")
print("   Manager is a subclass of Employee:", issubclass(Manager, Employee))
print("   manager1 is an Employee:", isinstance(manager1, Employee))
print("   get_name comes from Employee and still works:", manager1.get_name())
print("   set_department comes from Employee and still works:")
manager1.set_department("Finance")
print("   department is now", manager1.get_department())


print("")
print("Test 4: new method give_raise (only Manager has it)")
print("   Employee has give_raise:", hasattr(Employee, "give_raise"))
print("   salary before:", money(manager2.get_salary()))
manager2.give_raise(10)
print("   after a 10 percent raise:", money(manager2.get_salary()))
manager2.give_raise(2.5)
print("   after a 2.5 percent raise:", money(manager2.get_salary()))


print("")
print("Test 5: overriding get_position")
employee = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
print("   Employee get_position:", employee.get_position())
print("   Manager get_position:", manager1.get_position())
print("   Employee version on the manager:", Employee.get_position(manager1))
manager3 = Manager("Pat Lee", 10001)
print("   Manager with no position:", manager3.get_position())


print("")
print("Test 6: bad values should be refused and the object should stay the same")
try:
    manager1.set_salary("a lot")
except TypeError as e:
    print("   refused:", e)

try:
    manager1.set_salary(-100)
except ValueError as e:
    print("   refused:", e)

try:
    manager1.give_raise(-5)
except ValueError as e:
    print("   refused:", e)

try:
    manager1.set_id_number("47899")
except TypeError as e:
    print("   refused:", e)

try:
    bad_manager = Manager("Bad Data", 5, "IT", "Lead", "free")
except TypeError as e:
    print("   refused:", e)

print("   manager 1 is still", manager1.get_name(), money(manager1.get_salary()))
