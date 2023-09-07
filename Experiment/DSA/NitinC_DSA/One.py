def find_max_value(arr):
    if len(arr) == 0:
        print("The input array is empty :)")
        return 0

    max_val = arr[0]

    for i in arr:
        if i > max_val:
            max_val = num
    print(str(max_val) + " is the maximum value in the array")
    return 1

# Taking input from the user
n = input("Enter the size of the array: ")
N = int(n)
array = []

for i in range(0,N,1):
    num = int(input("Enter a number: "))
    array.append(num)

# Call the function to find and print the maximum value
find_max_value(array)
