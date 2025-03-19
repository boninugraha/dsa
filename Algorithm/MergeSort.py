def merge(arr1, arr2):
    temp = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i += 1
        else:
            temp.append(arr2[j])
            j += 1
    while i < len(arr1):
        temp.append(arr1[i])
        i += 1

    while j < len(arr2):
        temp.append(arr2[j])
        j += 1

    return temp


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


# arr1 = [3, 4, 5, 6]
# arr2 = [1, 2, 7, 9]
# print(merge(arr1, arr2))

my_list = [4, 2, 6, 5, 1, 3, 0, 15, 100, -1, 105]
print(merge_sort(my_list))
