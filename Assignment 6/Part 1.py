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


def main():
    """Ask user for text, encode it and display result."""
    user_text = input("Enter letters: ")

    try:
        result = encode(user_text)
        print("Encoded:", result)
    except (TypeError, ValueError) as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()
