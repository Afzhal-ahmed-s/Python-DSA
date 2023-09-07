# Take as input S, a string.
# Write a function that inserts between each pair of characters the difference between their ascii codes.
# Print the value returned.

#   "01234"
S = "abdgh"

def customeSolution(S):

    myList = list(S)

    answer = []
    answer.append(myList[0])

    for i in range(1,len(myList)):
        answer.append( ord(myList[i-1]) - ord(myList[i]) )
        answer.append(myList[i])

    return answer

answer = customeSolution(S)

for i in range (len(answer)):
    print(answer[i], end=" ")

