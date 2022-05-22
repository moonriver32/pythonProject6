my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
from collections import Counter

c = Counter(my_list)
duplicates = [x for x in my_list if c[x] > 1]
print(duplicates)
new_list = [x for x in my_list if x not in duplicates]
print(new_list)
