class Matrix:
    def __init__(self, list1):
        self.str1 = list1

    def __str__(self):
        return f"{self.str1[0]}\n{self.str1[1]}"

    def __add__(self, other):
        sum_ = []

        for item in zip(self.str1, other.str1):
            sum_.append([sum([n, n1]) for n, n1 in zip(*item)])

        return Matrix(sum_)


a = Matrix([[9, 9], [9, 9]])
b = Matrix([[1, 1], [1, 1]])
a.str1

b.str1

print(a.str1)
print(b.str1)
print(a)
print(b)
print(a + b)
