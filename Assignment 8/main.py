import csv

CUSTOMERSFILE = "customers.txt"


def find_column(headings, names):
    "Find which column has the data we want"
    for name in names:
        if name in headings:
            return headings.index(name)

    raise ValueError("Could not find a " + names[0] + " column")


def load_customers(file_name):
    "Read the file and put each customer in a list as a tuple (company, contact, phone)"
    with open(file_name, "r") as file:
        lines = file.readlines()

    if len(lines) < 2:
        raise ValueError("Need a heading row and at least one customer")

    "Tabs or commas, whichever the first line has"
    if "\t" in lines[0]:
        splitter = "\t"
    else:
        splitter = ","

    rows = list(csv.reader(lines, delimiter=splitter))

    headings = []
    for heading in rows[0]:
        headings.append(heading.strip().lower().replace(" ", ""))

    company_pos = find_column(headings, ("companyname", "customername"))
    contact_pos = find_column(headings, ("contactname",))
    phone_pos = find_column(headings, ("phone", "phonenumber"))

    customers = []
    for row in rows[1:]:
        if "".join(row).strip() == "":
            continue
        if len(row) <= company_pos or len(row) <= contact_pos or len(row) <= phone_pos:
            raise ValueError("A row is missing columns: " + str(row))

        customer = (row[company_pos].strip(), row[contact_pos].strip(), row[phone_pos].strip())
        customers.append(customer)

    return customers


def swap_order(customers):
    "Put the contact name first in each tuple"
    swapped = []
    for customer in customers:
        swapped.append((customer[1], customer[0], customer[2]))

    return swapped


def sort_by_company(customers):
    "Sort by company name"
    return sorted(customers)


def sort_by_contact(customers):
    "Sort by contact name, contact name ends up first in the tuple"
    return sorted(swap_order(customers))


def search_customers(customers, text, position):
    "Find customers where the name has the text in it, position 0 is company and 1 is contact"
    matches = []
    for customer in customers:
        if text.lower() in customer[position].lower():
            matches.append(customer)

    return matches


def display_customers(first_title, second_title, rows):
    "Print the customers, first_title and second_title are the first two column names"
    print("")
    print(first_title, "|", second_title, "|", "Phone")
    print("--------------------")
    for row in rows:
        print(row[0], "|", row[1], "|", row[2])

    print("")
    print("Customers found:", len(rows))


def do_search(customers, position):
    "Ask what to search for then show the matches"
    if position == 0:
        text = input("Enter part of a company name: ").strip()
    else:
        text = input("Enter part of a contact name: ").strip()

    if text == "":
        print("Please enter something to search for")
        return

    matches = search_customers(customers, text, position)

    if len(matches) == 0:
        print("No customers found for", text)
    elif position == 0:
        display_customers("Company Name", "Contact Name", sorted(matches))
    else:
        display_customers("Contact Name", "Company Name", sorted(swap_order(matches)))


def show_menu():
    "Print the menu"
    print("")
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")


def main():
    "Load the customers then keep showing the menu until the user picks 5"
    try:
        customers = load_customers(CUSTOMERSFILE)
    except FileNotFoundError:
        print("Could not find", CUSTOMERSFILE, "- put it in the same folder as this program")
        return
    except ValueError as e:
        print("Problem with", CUSTOMERSFILE, ":", e)
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_customers("Company Name", "Contact Name", sort_by_company(customers))
        elif choice == "2":
            display_customers("Contact Name", "Company Name", sort_by_contact(customers))
        elif choice == "3":
            do_search(customers, 0)
        elif choice == "4":
            do_search(customers, 1)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Please enter a number from 1 to 5")


main()
