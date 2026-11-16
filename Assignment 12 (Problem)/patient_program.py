import datetime

from patient import Patient
from procedure import Procedure


def money(amount):
    "puts a dollar sign and 2 decimals on an amount"
    return "$" + format(amount, ".2f")


def show_patient(patient):
    "prints the patient information"
    name = patient.get_first_name()
    if patient.get_middle_name()!="":
        name = name + " " + patient.get_middle_name()
    name = name + " " + patient.get_last_name()

    print("   name:", name)
    print("   address:", patient.get_address() + ",", patient.get_city() + ",", patient.get_state(), patient.get_zip_code())
    print("   phone:", patient.get_phone())
    print("   emergency contact:", patient.get_emergency_name() + ",", patient.get_emergency_phone())


def show_procedure(procedure):
    "prints the information for one procedure"
    print("   procedure:", procedure.get_name())
    print("   date:", procedure.get_date())
    print("   practitioner:", procedure.get_practitioner())
    print("   charges:", money(procedure.get_charges()))


print("Patient")
patient = Patient("Jane", "Marie", "Doe", "123 Maple Street", "Springfield", "IL", "62704", "217-555-0142", "John Doe", "217-555-0187")
show_patient(patient)


print("")
print("Procedures")
today = str(datetime.date.today())
procedure1 = Procedure("Physical Exam", today, "Dr. Irvine", 250.00)
procedure2 = Procedure("X-ray", today, "Dr. Jamison", 500.00)
procedure3 = Procedure("Blood test", today, "Dr. Smith", 200.00)
procedures = [procedure1, procedure2, procedure3]

total = 0
for i in range(len(procedures)):
    print("")
    print("Procedure #" + str(i+1))
    show_procedure(procedures[i])
    total = total + procedures[i].get_charges()

print("")
print("Total charges:", money(total))
if total==950.00:
    print("   that matches 250.00 + 500.00 + 200.00")
else:
    print("   that is NOT 950.00")


print("")
print("Test: the mutators change the data")
patient.set_phone("217-555-0100")
patient.set_middle_name("")
procedure3.set_charges(210)
print("   phone is now", patient.get_phone())
print("   middle name is now", repr(patient.get_middle_name()))
print("   blood test charges are now", money(procedure3.get_charges()))


print("")
print("Test: bad values should be refused")
try:
    patient.set_zip_code(62704)
except TypeError as e:
    print("   refused:", e)

try:
    bad_patient = Patient("Bad", "Data", 5, "1 St", "Town", "IL", "62704", "217-555-0000", "Kin", "217-555-0001")
except TypeError as e:
    print("   refused:", e)

try:
    procedure1.set_charges(-20)
except ValueError as e:
    print("   refused:", e)

try:
    bad_procedure = Procedure("Scan", today, "Dr. Lee", "free")
except TypeError as e:
    print("   refused:", e)

print("   physical exam charges are still", money(procedure1.get_charges()))
