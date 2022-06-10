class Wrong_format(ValueError):

    def __init__(self, my_list: list):
        self.my_list = my_list


my_list = []
while True:
    try:
        element = input("введите число или слово stop(чтобы прервать процесс)")
        if element == "stop":
            break
        if not element.isdigit():
            raise Wrong_format(element)
        my_list.append(int(element))
    except Wrong_format:
        print('формат нечисловой')
print(my_list)
