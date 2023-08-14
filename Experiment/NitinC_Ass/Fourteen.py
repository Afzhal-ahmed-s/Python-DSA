def spiral_print_clockwise(arr):
    if not arr:
        return

    rows, cols = len(arr), len(arr[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:

        # Print top row
        for col in range(left, right + 1, 1):
            print(arr[top][col], end=' ')
        top += 1

        # Print right column
        for row in range(top, bottom + 1, 1):
            print(arr[row][right], end=' ')
        right -= 1

        # Print bottom row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                print(arr[bottom][col], end=' ')
            bottom -= 1

        # Print left column
        if left <= right:
            for row in range(bottom, top - 1, -1):
                print(arr[row][left], end=' ')
            left += 1


input_array = [
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34],
    [41, 42, 43, 44]
]

spiral_print_clockwise(input_array)
