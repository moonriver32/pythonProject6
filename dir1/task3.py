x = int(input("введите число"))
y = int(input("введите число"))
z = int(input("введите число"))


def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    my_list.sort()
    return int(my_list[1]) + int(my_list[2])


print(my_func(x, y, z))
