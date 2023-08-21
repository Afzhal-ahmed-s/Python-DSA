# Write a function that toggles the case of all characters in the string.

def toggleCaseInAString(str):
    length = len(str)

    for i in range(length):
        if ord (str[i:i+1]) >= 97:
            print(str[i:i+1].upper())
        else:
            print(str[i:i+1].lower())

toggleCaseInAString("AfzHal")