import sqlite3

DBFILE = "Northwind.db"
CHANGEABLE = ("Customers", "Employees", "Products")
MAXWIDTH = 25


def get_tables(cur):
    "gets the table names from the database and puts them in a list"
    if type(cur)!=sqlite3.Cursor:
        raise TypeError("cur must be a cursor")

    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
    tables = []
    for row in cur.fetchall():
        tables.append(row[0])

    return tables


def check_table(cur, table):
    "makes sure the table is a real table in the database"
    if type(table)!=str:
        raise TypeError("table must be a string")
    if table not in get_tables(cur):
        raise ValueError("no table called " + table)


def check_db(con, cur, table):
    "makes sure the connection, cursor and table are ok before changing anything"
    if type(con)!=sqlite3.Connection:
        raise TypeError("con must be a database connection")

    check_table(cur, table)


def get_rows(cur, table):
    "gets the column names (from cursor.description) and every row in the table"
    check_table(cur, table)

    cur.execute('SELECT * FROM "' + table + '" ORDER BY 1')
    names = []
    for item in cur.description:
        names.append(item[0])

    return names, cur.fetchall()


def get_columns(cur, table):
    "gets the rules for each column (name, type, not null, default, key) as a list of dictionaries"
    check_table(cur, table)

    columns = []
    for item in cur.execute('PRAGMA table_info("' + table + '")').fetchall():
        columns.append({"name": item[1], "type": item[2], "notnull": item[3], "default": item[4], "pk": item[5]})

    return columns


def value_text(value):
    "turns a value from the database into text we can print"
    if value is None:
        return "NULL"

    return str(value).replace("\n", " ")


def cut(text, width):
    "cuts text down to the width with ... on the end if it was too long"
    if len(text)>width:
        return text[:width-3] + "..."

    return text


def show_table(names, rows):
    "modify #1, prints the table with column names and row numbers"
    if type(names)!=list or type(rows)!=list:
        raise TypeError("names and rows must be lists")
    for row in rows:
        if len(row)!=len(names):
            raise ValueError("a row doesnt match the column names")

    "each column is as wide as its longest value but no wider than MAXWIDTH"
    widths = []
    for i in range(len(names)):
        width = len(names[i])
        for row in rows:
            width = max(width, len(value_text(row[i])))
        widths.append(min(width, MAXWIDTH))

    numwidth = max(3, len(str(len(rows))))

    "heading line"
    parts = ["Row".rjust(numwidth)]
    for i in range(len(names)):
        parts.append(cut(names[i], widths[i]).ljust(widths[i]))
    heading = " | ".join(parts)

    print("")
    print(heading)
    print("-" * len(heading))

    "one line for each row starting with its row number"
    for n in range(len(rows)):
        parts = [str(n+1).rjust(numwidth)]
        for i in range(len(names)):
            parts.append(cut(value_text(rows[n][i]), widths[i]).ljust(widths[i]))
        print(" | ".join(parts))

    print("")
    print("rows:", len(rows))


def ask_number(prompt, low, high):
    "asks for a whole number from low to high, keeps asking till its ok, blank gives back None"
    if type(prompt)!=str or type(low)!=int or type(high)!=int:
        raise TypeError("prompt must be a string, low and high must be whole numbers")
    if low>high:
        raise ValueError("low cant be more than high")

    while True:
        text = input(prompt).strip()
        if text=="":
            return None

        try:
            number = int(text)
        except ValueError:
            number = low-1

        if low<=number<=high:
            return number

        print("enter a number from", low, "to", high)


def check_date(name, text):
    "checks a date typed as YYYY-MM-DD and gives it back like the dates already in the table"
    parts = text.split("-")
    if len(parts)!=3 or len(parts[0])!=4 or len(parts[1])!=2 or len(parts[2])!=2:
        raise ValueError(name + " has to look like 1990-01-31")

    for part in parts:
        for letter in part:
            if letter not in "0123456789":
                raise ValueError(name + " has to look like 1990-01-31")

    if int(parts[1])<1 or int(parts[1])>12 or int(parts[2])<1 or int(parts[2])>31:
        raise ValueError(name + " has a month or day that is not real")

    return text + " 00:00:00"


def convert_value(column, text):
    "data validation, checks what was typed against the column rules and gives back the value to save"
    if type(column)!=dict or type(text)!=str:
        raise TypeError("column must be a dictionary and text must be a string")

    name = column["name"]
    kind = column["type"].upper()
    text = text.strip()

    "blank means nothing (NULL) but only if the column allows that"
    if text=="":
        if column["notnull"]==1:
            raise ValueError(name + " cant be empty")
        return None

    "whole number columns"
    if "INT" in kind:
        for letter in text:
            if letter not in "0123456789":
                raise ValueError(name + " has to be a whole number, 0 or more")
        value = int(text)
        if name=="Discontinued" and value>1:
            raise ValueError("Discontinued has to be 0 or 1")
        return value

    "decimal number columns"
    if "REAL" in kind:
        for letter in text:
            if letter not in "0123456789.":
                raise ValueError(name + " has to be a number like 12.50")
        try:
            return float(text)
        except ValueError:
            raise ValueError(name + " has to be a number like 12.50")

    "date columns are text in this database"
    if "Date" in name:
        return check_date(name, text)

    "text columns, nchar ( 5 ) means 5 characters at most"
    if "(" in column["type"]:
        limit = column["type"].split("(")[1].split(")")[0].strip()
        if limit.isdigit() and len(text)>int(limit):
            raise ValueError(name + " cant be longer than " + limit + " characters")

    return text


def ask_value(column, adding):
    "asks for one value and keeps asking till its ok, gives back (use default, value)"
    if type(column)!=dict or type(adding)!=bool:
        raise TypeError("column must be a dictionary and adding must be True or False")

    name = column["name"]
    hasdefault = column["default"] is not None

    "the note in the prompt says what blank does"
    if adding and hasdefault:
        note = "blank = " + str(column["default"])
    elif column["notnull"]==1:
        note = "required"
    else:
        note = "blank = empty"

    while True:
        text = input(name + " (" + note + "): ").strip()

        "when adding, blank on a column with a default just uses the default"
        if adding and hasdefault and text=="":
            return True, None

        try:
            return False, convert_value(column, text)
        except ValueError as e:
            print(e)


def find_key(columns):
    "finds which column is the primary key, gives back None if there isnt one"
    for i in range(len(columns)):
        if columns[i]["pk"]==1:
            return i

    return None


def insert_record(con, cur, table):
    "modify #2 insert, asks for each field, checks it, then adds the new record"
    check_db(con, cur, table)

    columns = get_columns(cur, table)
    names = []
    values = []
    autoname = None

    for column in columns:
        "an INTEGER key makes its own number so we dont ask for it"
        if column["pk"]==1 and column["type"].upper()=="INTEGER":
            autoname = column["name"]
            continue

        usedefault, value = ask_value(column, True)
        if not usedefault:
            names.append('"' + column["name"] + '"')
            values.append(value)

    marks = ",".join(["?"] * len(values))
    sql = 'INSERT INTO "' + table + '" (' + ",".join(names) + ") VALUES (" + marks + ")"

    try:
        cur.execute(sql, values)
        con.commit()
    except sqlite3.Error as e:
        con.rollback()
        print("cant add the record:", e)
        return

    if autoname is None:
        print("record added")
    else:
        print("record added,", autoname, "is", cur.lastrowid)


def show_record(columns, row):
    "prints every field of one row so the user can see the whole record"
    for i in range(len(columns)):
        print(" ", columns[i]["name"] + ":", value_text(row[i]))


def update_record(con, cur, table, rows):
    "modify #2 update, pick a row and a field, ask for the new value, then update the record"
    check_db(con, cur, table)
    if type(rows)!=list:
        raise TypeError("rows must be a list")
    if len(rows)==0:
        print("there are no rows to update")
        return

    columns = get_columns(cur, table)
    keypos = find_key(columns)
    if keypos is None:
        print("this table has no key so it cant be updated")
        return

    "pick the row"
    number = ask_number("row number to update (blank to cancel): ", 1, len(rows))
    if number is None:
        return
    row = rows[number-1]

    "show the fields, the key is left out because other tables use it"
    fields = []
    for i in range(len(columns)):
        if i!=keypos:
            fields.append(i)

    print("")
    for n in range(len(fields)):
        print(str(n+1) + ".", columns[fields[n]]["name"] + ":", value_text(row[fields[n]]))

    "pick the field and get the new value"
    choice = ask_number("field number to change (blank to cancel): ", 1, len(fields))
    if choice is None:
        return
    column = columns[fields[choice-1]]
    value = ask_value(column, False)[1]

    sql = 'UPDATE "' + table + '" SET "' + column["name"] + '"=? WHERE "' + columns[keypos]["name"] + '"=?'

    try:
        cur.execute(sql, (value, row[keypos]))
        con.commit()
    except sqlite3.Error as e:
        con.rollback()
        print("cant update the record:", e)
        return

    print("record updated")


def delete_record(con, cur, table, rows):
    "modify #2 delete, pick a row, make sure, then delete the record"
    check_db(con, cur, table)
    if type(rows)!=list:
        raise TypeError("rows must be a list")
    if len(rows)==0:
        print("there are no rows to delete")
        return

    columns = get_columns(cur, table)
    keypos = find_key(columns)
    if keypos is None:
        print("this table has no key so it cant be deleted from")
        return

    "pick the row and show it"
    number = ask_number("row number to delete (blank to cancel): ", 1, len(rows))
    if number is None:
        return
    row = rows[number-1]

    print("")
    show_record(columns, row)
    answer = input("delete this record? (y/n): ").strip().lower()
    if answer!="y":
        print("not deleted")
        return

    sql = 'DELETE FROM "' + table + '" WHERE "' + columns[keypos]["name"] + '"=?'

    try:
        cur.execute(sql, (row[keypos],))
        con.commit()
    except sqlite3.IntegrityError:
        con.rollback()
        print("cant delete, other tables (like orders) still use this record")
        return
    except sqlite3.Error as e:
        con.rollback()
        print("cant delete the record:", e)
        return

    print("record deleted")


def work_on_table(con, cur, table):
    "shows one table then lets the user insert, update or delete till they go back"
    check_db(con, cur, table)

    names, rows = get_rows(cur, table)
    show_table(names, rows)

    "only customers, employees and products can be changed"
    if table not in CHANGEABLE:
        print("only", ", ".join(CHANGEABLE), "can be changed")
        return

    while True:
        action = input("(I)nsert, (U)pdate, (D)elete or (B)ack: ").strip().lower()

        if action=="b":
            return
        elif action=="i":
            insert_record(con, cur, table)
        elif action=="u":
            update_record(con, cur, table, rows)
        elif action=="d":
            delete_record(con, cur, table, rows)
        else:
            print("enter i, u, d or b")
            continue

        "show the table again so the row numbers are right"
        names, rows = get_rows(cur, table)
        show_table(names, rows)


def main():
    "checks the database file, lists the tables and lets the user pick one"
    "connect would make a new empty file if the database was missing so check first"
    try:
        open(DBFILE, "rb").close()
    except FileNotFoundError:
        print("cant find", DBFILE, "- put it in the same folder as this program")
        return

    con = sqlite3.connect(DBFILE)
    cur = con.cursor()

    "SQLite doesnt check foreign keys unless we turn it on"
    cur.execute("PRAGMA foreign_keys = ON")

    try:
        tables = get_tables(cur)
    except sqlite3.DatabaseError as e:
        print("problem with", DBFILE, ":", e)
        con.close()
        return

    if len(tables)==0:
        print("no tables in", DBFILE, "- run northwind.sql first")
        con.close()
        return

    "list the tables and keep going till the user leaves"
    while True:
        print("")
        print("tables:")
        for i in range(len(tables)):
            print(str(i+1) + ".", tables[i])

        choice = ask_number("table number (blank to exit): ", 1, len(tables))
        if choice is None:
            break

        work_on_table(con, cur, tables[choice-1])

    con.close()
    print("bye")


main()
