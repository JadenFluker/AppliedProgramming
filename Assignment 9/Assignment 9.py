import csv

CUSTOMERSFILE = "customers.txt"
REQUIRED = ("CompanyName", "ContactName", "Phone")
COMPANYORDER = ("CompanyName", "ContactName", "Phone")
CONTACTORDER = ("ContactName", "CompanyName", "Phone")
LABELS = {"CompanyName": "Company", "ContactName": "Contact", "Phone": "Phone"}


def check_customers(customers, fields):
    "make sure customers is a list of dicts that all have the fields"
    if type(customers) != list:
        raise TypeError("customers must be a list")

    if type(fields) != tuple:
        raise TypeError("fields must be a tuple")

    for field in fields:
        if type(field) != str:
            raise TypeError("fields must be strings")

    for customer in customers:
        if type(customer) != dict:
            raise TypeError("each customer must be a dict")

        for field in fields:
            if field not in customer:
                raise ValueError("customer is missing " + field)
            if type(customer[field]) != str:
                raise TypeError(field + " must be a string")


def fix_row(row, headings):
    "put the address back together if it had a comma in it"
    extra = len(row) - len(headings)

    if extra > 0 and "Address" in headings:
        start = headings.index("Address")
        address = ",".join(row[start:start + extra + 1])
        row = row[:start] + [address] + row[start + extra + 1:]

    return row


def load_customers(file_name):
    "read the file and return a list of dicts, one per customer"
    if type(file_name) != str:
        raise TypeError("file_name must be a string")

    with open(file_name, "r", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    if len(rows) < 2:
        raise ValueError("need a heading row and a customer")

    headings = []
    for heading in rows[0]:
        headings.append(heading.strip())

    for name in REQUIRED:
        if name not in headings:
            raise ValueError("no " + name + " column")

    customers = []
    for row in rows[1:]:
        "skip blank lines"
        if "".join(row).strip() == "":
            continue

        row = fix_row(row, headings)
        if len(row) != len(headings):
            raise ValueError("bad row: " + str(row))

        customer = {}
        for i in range(len(headings)):
            customer[headings[i]] = row[i].strip()

        customers.append(customer)

    if len(customers) == 0:
        raise ValueError("no customers in file")

    return customers


def sort_customers(customers, field):
    "sort customers by the field, ignores capitals"
    check_customers(customers, (field,))

    "pair each name with its spot so it can be sorted"
    pairs = []
    for i in range(len(customers)):
        pairs.append((customers[i][field].lower(), i))

    pairs.sort()

    sorted_customers = []
    for name, i in pairs:
        sorted_customers.append(customers[i])

    return sorted_customers


def search_customers(customers, field, text):
    "find customers with the text in the field, ignores capitals"
    check_customers(customers, (field,))

    if type(text) != str:
        raise TypeError("text must be a string")
    if text.strip() == "":
        raise ValueError("text is empty")

    matches = []
    for customer in customers:
        if text.lower() in customer[field].lower():
            matches.append(customer)

    return matches


def display_customers(customers, fields):
    "print customers with labels, fields is the order to show them"
    check_customers(customers, fields)

    print("")
    for customer in customers:
        parts = []
        for field in fields:
            if field in LABELS:
                label = LABELS[field]
            else:
                label = field
            parts.append(label + ": " + customer[field])

        print(" | ".join(parts))

    print("")
    print("found:", len(customers))


def do_search(customers, field):
    "ask for text then show the matches"
    if field == "CompanyName":
        text = input("company name: ").strip()
        fields = COMPANYORDER
    else:
        text = input("contact name: ").strip()
        fields = CONTACTORDER

    if text == "":
        print("type something")
        return

    matches = search_customers(customers, field, text)

    if len(matches) == 0:
        print("none found for", text)
    else:
        display_customers(sort_customers(matches, field), fields)


def show_menu():
    "print the menu"
    print("")
    print("1. customers by company name")
    print("2. customers by contact name")
    print("3. search company name")
    print("4. search contact name")
    print("5. exit")


def main():
    "load customers then keep showing the menu till exit"
    try:
        customers = load_customers(CUSTOMERSFILE)
    except FileNotFoundError:
        print("cant find", CUSTOMERSFILE)
        return
    except ValueError as e:
        print("problem with", CUSTOMERSFILE, ":", e)
        return

    while True:
        show_menu()
        choice = input("choose 1-5: ").strip()

        if choice == "1":
            display_customers(sort_customers(customers, "CompanyName"), COMPANYORDER)
        elif choice == "2":
            display_customers(sort_customers(customers, "ContactName"), CONTACTORDER)
        elif choice == "3":
            do_search(customers, "CompanyName")
        elif choice == "4":
            do_search(customers, "ContactName")
        elif choice == "5":
            print("bye")
            break
        else:
            print("pick 1 to 5")


main()
