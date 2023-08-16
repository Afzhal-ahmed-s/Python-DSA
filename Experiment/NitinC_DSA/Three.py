import math

print("It's Binary search.")

array = [10,20,30,40,50,60,70,80,90,100]

num = input("Enter the number: ")
number = int(num)

def binary_search(array, number):
    l = 0
    r = len(array) - 1
    mid = math.floor((l+r)/2)
    iteration = 0

    if(number > array[r] or number < array[l]):
        return -1

    while(mid <= r and mid >= l):
        mid = math.floor((l+r)/2)

        if(array[mid] == number):
            return mid
        elif(array[mid] < number):
            l = mid + 1
            mid = math.floor((l + r) / 2)
        else:
            r = mid - 1
            mid = math.floor((l + r) / 2)

        iteration+=1
        print("Iteration: "+ str(iteration))

    else:
        return -1


index = binary_search(array, number)
print("The index of the number "+ str(number)+" is "+str(index) +" in the array.")