my_list = [4, 2, 6, 5, 1, 3, 0, 15, 100, -1, 105]


def bubble_sort(arr):
    counter = 0
    for i in range(len(arr) - 1):
        # print(len(arr) - i - 1)
        for j in range(len(arr) - i - 1):
            # print(f"{my_list[j]} and {my_list[j+1]}")
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    #         counter += 1
    # print(counter)
    return arr


def bubble_sort2(my_list):
    # counter = 0
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            # counter += 1
    # print(counter)
    return my_list


print(bubble_sort(my_list))
print(bubble_sort2(my_list))
