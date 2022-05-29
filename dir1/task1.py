def my_func(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        return ("Выберите число, отличное от 0")


a = int(input("Введите число"))
b = int(input("Введите число"))
print(my_func(a, b))
