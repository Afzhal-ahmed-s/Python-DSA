array = [10,20,30,40,50,60,70,80,90,100]

num = input("Enter the number: ")
number = int(num)

def find_number_in_array(array):
    for i in range(0, len(array)):
        if number == array[i]:
            return i

    return -1

print("The index of the number "+ str(number)+" is "+str(find_number_in_array(array)) +" in the array.")