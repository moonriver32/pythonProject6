my_file = open('data_file1.txt', 'w+')

with open('data_file1.txt', 'w+') as f:
    print('1 9 ', file=f)
with open('data_file1.txt', 'r') as f:
    for x in f:
        x = x.rstrip()
        my_list = list(x)
        filt = [x for x in my_list if x != ' ']
        print("сумма чисел=", sum([int(x) for x in filt]))
z = sum([int(x) for x in filt])
with open('data_file1.txt', 'a') as f:
    print("sum=", z, file=f)

my_file.close()
