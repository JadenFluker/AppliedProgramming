
courses = {
    "Python": {"Alice", "Bob", "Charlie", "David"},
    "Database": {"Bob", "Eve", "Frank", "Alice"},
    "Networking": {"Charlie", "George", "Alice"},
    "Cybersecurity": {"David", "Eve", "Henry", "Charlie"}
}

print("Course Enrollments")
print("------------------")
for course in courses:
    print(course + ":", courses[course])

print("")
print("Number of students in each course:")
for course in courses:
    print(course + ":", len(courses[course]), "students")


python_database = courses["Python"].intersection(courses["Database"])
python_cyber = courses["Python"].intersection(courses["Cybersecurity"])

print("")
print("Students in Python and Database:")
print(python_database)

print("")
print("Students in Python and Cybersecurity:")
print(python_cyber)


all_students = set()
for course in courses:
    all_students = all_students.union(courses[course])

print("")
print("All Unique Students:")
print(all_students)
print("Total unique students:", len(all_students))


only_one = set()
for course in courses:
    others = set()
    for other_course in courses:
        if other_course!=course:
            others = others.union(courses[other_course])

    only_one = only_one.union(courses[course].difference(others))

print("")
print("Students Taking Only One Course:")
print(only_one)


print("")
name = input("Enter student name: ").strip()
print("")

enrolled = []
for course in courses:
    if name in courses[course]:
        enrolled.append(course)

if len(enrolled)>0:
    print(name, "is enrolled in:")
    for course in enrolled:
        print(course)
else:
    print("Student not found.")
