# Write a function that replaces every odd character with the character
# having just higher ascii code and every even character with the character
# having just lower ascii code. Remember that strings are immutable.

#indexing
#   "012345"
s = "Abcde"

def customSolution(s):
    myList = list(s)

    for i in range(len(myList)):
        if i % 2 == 0 :
            myList[i] = chr( ord(myList[i]) - 1 )
        else:
            myList[i] = chr(ord(myList[i]) + 1)

        print(f"Check: {i}", myList[i])

customSolution(s)

