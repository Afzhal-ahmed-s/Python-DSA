# lambda, filter, map, reduce, list comprehension
from functools import reduce

input = [1,2,3,4,5,6,7,8,9,10]

def filterEvens(n):
    return n%2 == 0

def twiceTheNumber(n):
    return n*2

def sum(a, b):
    return a+b

evenNumbers = list(filter(filterEvens, input))
mapped = list( map(twiceTheNumber, evenNumbers) )
reduced = reduce(sum, mapped)

print("After filter: ",evenNumbers)
print("After mapping: ",mapped)
print("After reduction: ", reduced)

