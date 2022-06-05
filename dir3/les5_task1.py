with open('data_file5.txt', 'w') as printable:
    x = 0
    while x != '':
        x = input("введите текст и затем Enter\n")
        print(x, file=printable)
