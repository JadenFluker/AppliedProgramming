ENCODED_MARKER = "##00"
def encode(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    encoded = ENCODED_MARKER
    i = 0
    while i < len(text):
        char = text[i]
        count = 1
        while i + count < len(text) and text[i + count] == char:
            count += 1

        if char.isdigit() or char == "#":
            token = "#" + char
        else:
            token = char
        encoded += token if count == 1 else token + str(count)
        i += count
    return encoded
def decode(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text.startswith(ENCODED_MARKER):
        raise ValueError("text is not valid RLE format")

    decoded = ""
    i = 0
    while i < len(text):
        char = text[i]

        if char == "#":
            i += 1
            if i >= len(text):
                raise ValueError("text is not valid RLE format")
            literal_char = text[i]
            i += 1
        else:
            literal_char = char
            i += 1

        digits = ""
        while i < len(text) and text[i].isdigit():
            digits += text[i]
            i += 1
        count = int(digits) if digits else 1

        decoded += literal_char * count

    return decoded


def is_encoded(text):
    return text.startswith(ENCODED_MARKER)
def main():
    """Asks for string, encode or decode it."""
    user_text = input("Enter a string: ")

    try:
        if is_encoded(user_text):
            result = decode(user_text)
            print("Already encoded. Decoded:", result)
        else:
            result = encode(user_text)
            print("Encoded:", result)
    except (TypeError, ValueError) as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()
