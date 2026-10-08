NAMESFILE = "names.txt"
NOTFOUNDFILE = "nofound.txt"


def load_names(file_name):

    if not isinstance(file_name, str) or file_name == "":
        raise ValueError("file_name must be a non-empty string")

    names = []
    with open(file_name, "r") as file:
        for line in file:
            name = line.strip()
            if name != "":
                names.append(name)

    return names


def is_name_in_list(name, names):

    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if not isinstance(names, list):
        raise TypeError("names must be a list")

    for existing_name in names:
        if existing_name.lower() == name.lower():
            return True

    return False


def write_not_found(file_name, name):

    if not isinstance(file_name, str) or file_name == "":
        raise ValueError("file_name must be a non-empty string")
    if not isinstance(name, str) or name == "":
        raise ValueError("name must be a non-empty string")

    with open(file_name, "a") as file:
        file.write(name + "\n")


def main():
    try:
        names = load_names(NAMESFILE)
    except FileNotFoundError:
        print("Could not find", NAMESFILE, "- put it in the same folder as this program.")
        return
    except OSError as e:
        print("Could not read", NAMESFILE, ":", e)
        return

    while True:
        user_name = input("Enter a name (or type quit to stop): ").strip()

        if user_name == "":
            print("Please enter a name.")
        elif user_name.lower() == "quit":
            break
        elif is_name_in_list(user_name, names):
            print(user_name, "was found in the file.")
        else:
            try:
                write_not_found(NOTFOUNDFILE, user_name)
                print(user_name, "was not found. It was written to", NOTFOUNDFILE)
            except OSError as e:
                print("Could not write to", NOTFOUNDFILE, ":", e)


if __name__ == "__main__":
    main()
