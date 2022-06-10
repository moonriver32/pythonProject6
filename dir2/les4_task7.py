def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
        yield f


n = 10
for number in fact(n):
    print(number)
