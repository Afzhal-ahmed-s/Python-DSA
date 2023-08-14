import math

array = [10,20,30,40,50,60,70,80,90,100]

def swap(array):
    length = len(array)
    for i in range(0, math.floor(length/2), 1):
        transferWindow = array[i]
        array[i] = array[length-i-1]
        array[length - i-1] = transferWindow

    return array

reversedArray = swap(array)

print(reversedArray)