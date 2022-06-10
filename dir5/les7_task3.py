class Element:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity - other.quantity >= 0:
            return self.quantity - other.quantity
        else:
            return f"операцию вычитания выполнить нельзя"

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, count=4):
        self.count = count
        for i in range(self.quantity // self.count):
            print(f"*" * self.count)
        rez = self.quantity - (self.quantity // self.count * self.count)
        if rez > 0:
            print(f"*" * rez)
        else:
            print("")


element1 = Element(30)
element2 = Element(3)
element1.quantity
element2.quantity

print(element1 + element2)
print(element1 - element2)
print(element1 * element2)
print(element1 / element2)
element1.make_order(7)
