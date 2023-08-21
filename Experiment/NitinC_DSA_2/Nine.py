# Take as input S, a string. Write a function that removes all consecutive duplicates.
# Print the value returned. E.g. for input "aabccba" print "abcba".

def removeDuplicates(S):
    length = len(S)
    myList = []
    i = 0
    print("len: ",length)

    while i < length:
        myList.append(S[i])
        while i+1 < length  and S[i] == S[i + 1]:
            i += 1
        i += 1
        print(i)
    return "".join(myList)

input = "aabccbaa"
print( removeDuplicates(input) )