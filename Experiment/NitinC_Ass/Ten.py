def add_arrays(arr1, arr2):
    # Make the lengths of the arrays equal by adding leading zeros
    length = max(len(arr1), len(arr2))
    arr1 = ([0] * (length - len(arr1))) + arr1
    arr2 = ([0] * (length - len(arr2))) + arr2

    carry = 0
    result = []

    for i in range(length - 1, -1, -1):
        total = arr1[i] + arr2[i] + carry
        carry = total // 10
        result.insert(0, total % 10)

    if carry:
        result.insert(0, carry)

    return result


array1 = [1, 0, 2, 7]
array2 = [3, 4, 5, 6, 3]
result = add_arrays(array1, array2)
print(result)