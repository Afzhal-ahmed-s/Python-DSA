# Write a function that returns the count of substrings of this string which are palindromes.

def is_palindrome(S):

  n = len(S)
  S = S.upper()

  for i in range(n // 2):
    if S[i] != S[n - i - 1]:
      return False

  return True

def produceSubStringCount(str):
    length = len(str)
    count = 0

    for i in range(0, length, 1):
        for j in range (i, length, 1):
            if j-i !=0 and is_palindrome(str[i:j+1]):
                count += 1
                print("The plaindromes are: ",str[i:j+1])

    return count

str = "abcbd"
answer = produceSubStringCount(str)

print(answer)