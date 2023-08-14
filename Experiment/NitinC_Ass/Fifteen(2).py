def plotTheGraphAndPrintIt(input_list):
    length_of_input = len(input_list)
    list_of_ten_string_s = ["", "", "", "", "", "", "", "", "", ""]

    for i in range(length_of_input):
        resourceAllocator(i, input_list[i], list_of_ten_string_s)

    for k in range(len(list_of_ten_string_s) - 1, -1, -1):
        print(f"s{k}| {list_of_ten_string_s[k]}")

    print("_________________________")
    print("/   0 1 2 3 4 5 6 7 8 9 ")

    return 0


def resourceAllocator(i, value, list_of_ten_string_s):
    length_of_ten_string_s = len(list_of_ten_string_s)

    list_of_ten_string_s[value]= list_of_ten_string_s[value] + "* "

    for j in range(0, value):
        list_of_ten_string_s[j] += "  "
    for j in range(value + 1, length_of_ten_string_s):
        list_of_ten_string_s[j] += "  "


input_list = [1, 2, 3, 2, 1, 0, 1, 2]
plotTheGraphAndPrintIt(input_list)
