def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

unsorted_array = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted Array:", unsorted_array)

print("Bubble sorted Array:", bubble_sort(unsorted_array))
print("Selection sorted Array:", selection_sort(unsorted_array))
print("Insertion sorted Array:", insertion_sort(unsorted_array))




