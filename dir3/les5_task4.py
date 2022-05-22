my_file = open(r'data_file4.txt', 'r')
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

for line in my_file.readlines():
    splitted = line.split()
    with open('data_file4_1.txt', 'a') as new_file:
        print(my_dict[splitted[0]], splitted[1], splitted[2], file=new_file)
my_file.close()
