# Take as input S, a string. Write a function that does basic string compression.
# Print the value returned. E.g. for input "aaabbccds" print out a3b2c2ds.

def compressString(s):
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    compressed.append(s[len(s)-1] + str(count))
    return ''.join(compressed)

input_str = "aaabbccds"
print(compressString(input_str))
