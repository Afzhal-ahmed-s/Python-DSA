# lambda, filter, map, reduce, list comprehension
from functools import reduce

input = [1,2,3,4,5,6,7,8,9,10]

evenNumbers = list(filter(lambda e : e%2 == 0, input))
mapped = list( map(lambda e : e*2, evenNumbers) )
reduced = reduce(lambda a, b: a+b, mapped)

print("After filter w/lambda: ",evenNumbers)
print("After mapping w/lambda: ",mapped)
print("After reduction w/lambda: ", reduced)

