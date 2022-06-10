my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [el for n, el in enumerate(my_list) if my_list[n - 1] < my_list[n]]

print(new_list[1:])

new_list1=[n for n in range(len(my_list)) if my_list[n - 1] < my_list[n] ]
print(new_list1[1:])