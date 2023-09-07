# Take as input S, a string. Write a function that prints all its permutations.

def permutations(s, start=0):
    if start == len(s) - 1:
        print(''.join(s))
        return

    for i in range(start, len(s)):
        s[start], s[i] = s[i], s[start]  # Swap characters
        print("Check: ",i, start)
        permutations(s, start + 1)  # Recurse for the next position
        s[start], s[i] = s[i], s[start]  # Backtrack by swapping again


input_str = input("Enter a string: ")
permutations(list(input_str))
