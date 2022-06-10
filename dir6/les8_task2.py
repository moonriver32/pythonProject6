class ZeroDivisionError(Exception):
    try:
        a = int(input("введите числовое значение делимого"))
        b = int(input("введите числовое значение делителя"))
        res = a / b
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    else:
        print(f"Пример корректен. Результат: {res}")
