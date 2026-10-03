def encode(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text.isalpha():
        raise ValueError("text must contain only letters")

    encoded = ""
    i = 0
    while i < len(text):
        char = text[i]
        count = 1
        while i + count < len(text) and text[i + count] == char:
            count += 1
        encoded += char if count == 1 else char + str(count)
        i += count

    return encoded


def decode(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    decoded = ""
    i = 0
    while i < len(text):
        char = text[i]
        if not char.isalpha():
            raise ValueError("text is not valid RLE format")
        i += 1

        digits = ""
        while i < len(text) and text[i].isdigit():
            digits += text[i]
            i += 1
        count = int(digits) if digits else 1

        decoded += char * count

    return decoded


def has_numbers(text):
    for char in text:
        if char.isdigit():
            return True
    return False


def main():
    user_text = input("Enter a string: ")

    try:
        if has_numbers(user_text):
            result = decode(user_text)
            print("Already encoded. Decoded:", result)
        else:
            result = encode(user_text)
            print("Encoded:", result)
    except (TypeError, ValueError) as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()
