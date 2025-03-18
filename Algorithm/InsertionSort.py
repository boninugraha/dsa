def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]  # initial value
        j = i - 1  # 1 value before the initial value
        while (
            temp < arr[j] and j >= 0
        ):  # while the previous value is smaller than the iniial value
            arr[j + 1] = arr[j]  # get the previous value and move it forward
            arr[j] = temp  # move the initial value into the previous position
            j -= 1  # move the j to the left 1 time
    return arr


my_list = [4, 2, 6, 5, 1, 3, 0, 15, 100, -1, 105]
print(insertion_sort(my_list))
