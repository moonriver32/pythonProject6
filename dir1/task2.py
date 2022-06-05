# вариант1
my_list = ["Ivanov", "Ivan", 1987, "Samara", "old@mail.ru"]


def my_func(arg1):
    for i in my_list:
        print(i, end=" ")


my_func(arg1=my_list)

# вариант2
print()
surname = "Petrov"
name = "Petr"
born = 1985
mail = "lll@mail.ru"
city = "Orenburg"


def my_func2(arg_surname, arg_name, arg_born, arg_mail, arg_city):
    print(arg_surname, arg_name, arg_born, arg_mail, arg_city)


my_func2(arg_surname=surname, arg_name=name, arg_born=born, arg_mail=mail, arg_city=city)
