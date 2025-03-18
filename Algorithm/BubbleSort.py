my_list = [4, 2, 6, 5, 1, 3, 0, 15, 100, -1, 105]

for i in range(len(my_list) - 1):
    for j in range(len(my_list) - i - 1):
        # print(f"{my_list[j]} and {my_list[j+1]}")
        if my_list[j] > my_list[j + 1]:
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp

print(my_list)
