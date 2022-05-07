word = input("Введите слово")


def int_func(arg_word):
    return arg_word.capitalize()


print(int_func(word))

words = input("Введите несколько слов с маленькой буквы")


def int_func2(arg_words):
    my_list = arg_words.split()
    for i in my_list:
        print(int_func(i), end=" ")


int_func2(words)
