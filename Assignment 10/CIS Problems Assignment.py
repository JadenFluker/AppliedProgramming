import re


print("Problem 1")
tests = ["ABCDEFabcdef123450", "*&%@#!}{"]
for test in tests:
    if re.match(r"^[a-zA-Z0-9]+$", test):
        print(test, "-> matched")
    else:
        print(test, "-> not matched")


print("")
print("Problem 2")
tests = ["ab", "abc", "a", "ab", "abb"]
for test in tests:
    m = re.search(r"ab*", test)
    if m:
        print(test, "-> matched:", m.group())
    else:
        print(test, "-> not matched")


print("")
print("Problem 3")
tests = ["ab", "abc", "a", "ab", "abb"]
for test in tests:
    m = re.search(r"ab+", test)
    if m:
        print(test, "-> matched:", m.group())
    else:
        print(test, "-> not matched")


print("")
print("Problem 4")
tests = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]
for test in tests:
    if re.match(r"^[a-z]+_[a-z]+$", test):
        print(test, "-> matched")
    else:
        print(test, "-> not matched")


print("")
print("Problem 5")
tests = ["The quick brown fox jumps over the lazy dog.", " The quick brown fox jumps over the lazy dog."]
for test in tests:
    m = re.match(r"\w+", test)
    if m:
        print(repr(test), "-> matched:", m.group())
    else:
        print(repr(test), "-> not matched")


print("")
print("Problem 6")
tests = ["The quick brown fox jumps over the lazy dog.", "Python Exercises."]
for test in tests:
    words = re.findall(r"\w*z\w*", test)
    if len(words)>0:
        print(repr(test), "-> matched:", words)
    else:
        print(repr(test), "-> not matched")


print("")
print("Problem 7")
tests = ["216.08.094.196", "10.0.0.1", "010.000.001.100"]
for test in tests:
    print(test, "->", re.sub(r"\b0+(?=\d)", "", test))


print("")
print("Problem 8")
text = "The quick brown fox jumps over the lazy dog."
words = ["fox", "dog", "horse"]
for word in words:
    if re.search(word, text):
        print(word, "-> found")
    else:
        print(word, "-> not found")


print("")
print("Problem 9")
text = "The quick brown fox jumps over the lazy dog."
m = re.search("fox", text)
if m:
    print("fox found at", m.start(), "to", m.end())
else:
    print("fox not found")


print("")
print("Problem 10")


def swap(match):
    if match.group()=="_":
        return " "
    else:
        return "_"


tests = ["Regular Expressions", "Code_Examples"]
for test in tests:
    print(test, "->", re.sub(r"[\s_]", swap, test))


print("")
print("Problem 11")
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
m = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", url)
if m:
    year, month, day = m.groups()
    print("year:", year)
    print("month:", month)
    print("day:", day)
else:
    print("no date found")


print("")
print("Problem 12")
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(re.findall(r"\b[ae]\w*", text))


print("")
print("Problem 13")
text = "Python Exercises, PHP exercises."
print(re.sub(r"[ ,.]", ":", text))


print("")
print("Problem 14")
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(re.findall(r"\b[ae]\w*", text))


print("")
print("Problem 15")
text = "Python      Exercises"
print(re.sub(r" +", " ", text))
