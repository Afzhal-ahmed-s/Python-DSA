def intersection_with_duplicates(arr1, arr2):
    arr1.sort()
    arr2.sort()

    intersection = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return intersection


def intersection_without_duplicates(arr1, arr2):
    arr1.sort()
    arr2.sort()

    intersection = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        # two supplement while loops to remove the duplicates
        while i+1 < len(arr1) and arr1[i] == arr1[i+1]:
            i += 1
        while j + 1 < len(arr2) and arr2[j] == arr2[j + 1]:
            j += 1

        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return intersection


array1 = [1, 2, 3, 1, 2, 4, 1]
array2 = [2, 1, 3, 1, 5, 2, 2]
result_without_duplicates = intersection_without_duplicates(array1, array2)
result_with_duplicates = intersection_with_duplicates(array1, array2)

print("Without duplicates: "+ str(result_without_duplicates))
print("With duplicates: "+ str(result_with_duplicates))
