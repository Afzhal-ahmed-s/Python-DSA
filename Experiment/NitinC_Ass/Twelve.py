def column_print_2d_array(arr):
    rows = len(arr)
    cols = len(arr[0])
    storage = ""
    for col in range(cols):
        if col % 2 == 0:
            for row in range(rows):
                storage = storage + str(arr[row][col]) + ", "
        else:
            for row in range(rows - 1, -1, -1):
                storage = storage + str(arr[row][col]) + ", "
    print("Answer: "+ storage)


input_array = [
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34],
    [41, 42, 43, 44]
]

column_print_2d_array(input_array)
