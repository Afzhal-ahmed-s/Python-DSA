# Take as input S, a string. Write a function that returns the character with maximum frequency. Print the value returned.

def max_char_frequency(S):

  char_frequency = {}
  for character in S:
    if character in char_frequency:
      char_frequency[character] += 1
    else:
      char_frequency[character] = 1


  max_char = ''
  max_count = 0
  for character, count in char_frequency.items():
    if count > max_count:
      max_char = character
      max_count = count

  return max_char


S = input("Enter a string: ")
max_char = max_char_frequency(S)
print("The character with maximum frequency is:", max_char)