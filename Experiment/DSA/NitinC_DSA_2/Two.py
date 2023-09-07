# Write a function that prints all substrings (aka subsequences) of given string.

def printSubStrings(str):
    length = len(str)

    for i in range(0, length, 1):
        for j in range (i, length, 1):
            print(str[i:j+1])

str = "abcde"
printSubStrings(str)