my_list = [4, 2, 6, 5, 1, 3, 0, 15, 100, -1, 105]


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            # print(f"{my_list[j]} and {my_list[j+1]}")
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


print(bubble_sort(my_list))
