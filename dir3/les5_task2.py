my_file = open('data_file2.txt', 'r')
lines = 0
for line in my_file:
    lines += 1
    word = 0
    letters = 0
    for j in line:
        if j != ' ' and letters == 0:
            word += 1
            letters = 1
        elif j == ' ':
            letters = 0
    print('в строке:', line, 'слова', word)
print('всего строк', lines)  # сколько строк

my_file.close()
