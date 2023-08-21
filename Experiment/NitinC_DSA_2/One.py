# Take as input S, a string. Write a function that returns true if the string is palindrome and false otherwise.

def is_palindrome(S):

  n = len(S)
  S = S.upper()

  for i in range(n // 2):
    if S[i] != S[n - i - 1]:
      return False

  return True

inputString = "Afzfa"
print(is_palindrome(inputString))