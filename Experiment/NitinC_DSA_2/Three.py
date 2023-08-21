# Write a function that returns all substrings of given string. Print the value returned.

def produceSubStrings(str):
    length = len(str)
    list = []

    for i in range(0, length, 1):
        for j in range (i, length, 1):
            list.append(str[i:j+1])

    return list

str = "abcde"
answer = produceSubStrings(str)
length = len(answer)

for i in range(length):
    print(answer[i])