def quick_sort(list_input):
    pivot = list_input[0]
    if len(list_input) == 1:
        return list_input
    left = []
    right = []
    for i in range(1, len(list_input)):
        x = list_input[i]
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    left.append(pivot)
    return quick_sort(left) + quick_sort(right)


my_list = [4, 2, 6, 5, 1, 3, 0, 15, 100, -1, 105]
print(quick_sort(my_list))
