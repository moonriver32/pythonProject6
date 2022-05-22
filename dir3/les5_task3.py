my_file = open('data_file3.txt')
smallzp_list = []
smallzp_sum = 0
for line in my_file.readlines():
    splitted = line.split()
    if float(splitted[1]) < 20000:
        print('менее 20000 получает - ', splitted[0], splitted[1])
        smallzp_list.append(splitted[1])
        smallzp_sum = smallzp_sum + float(splitted[1])
        average = smallzp_sum / len(smallzp_list)

my_file.close()
print('Средняя среди зарплат менее 20 тыс. - ', average)
