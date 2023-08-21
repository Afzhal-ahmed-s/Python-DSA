# Why list comprehension
# Faster for loops
# Simplified conditional statements
# String manipulation
# Performance: In many cases, list comprehensions can be faster than traditional loops
# because they are optimized internally by Python's interpreter.



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
bits = [False, True, False, False, True]
input = [1,2,3,4,5,6,7,8,9,10]
input2 = [1,'a',2,'b',3,'c','3.2']
s = "ListComprehensionIsNotPureBliss"

# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

newList = [e if 'a' in e else 'e' for e in fruits]
print(newList)

numNewList = ["I'm Two" if e == 2 else e if e%2==0 else "Odd" for e in input]
print(numNewList)

newBits = [1 if e == True else 0 for e in bits]
print(newBits)

s = [i for i in s]
print(s)

s2 = "".join([i if i.islower() else " "+i if i in["C", "I", "N"] else " "+i.lower() for i in s])[1:]
print("S2: ",s2)

fruits = [e.upper() for e in fruits]
print(fruits)

[print(i) for i in input]

exp = list(map(lambda x: "I'm "+x, [f"{i} integer" if isinstance(i, int) else f"{i} float" if isinstance(i, float) else f"'{i}' str" for i in input2]))
print("Map + lambda + list comprehension: ",exp)

s3 = "Nitin"
print("s3: ",s3[::-1]) #reversing

# list of fruits
# check if apple is available in list
# class, pytest, assertion




