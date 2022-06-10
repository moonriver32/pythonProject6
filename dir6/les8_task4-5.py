class Office_equipment:
    def __init__(self, model, price, year):
        self.model = model
        self.price = price
        self.year = year
        self.printer_dict = {}
        self.scanner_dict = {}
        self.xerox_dict = {}


class Printer(Office_equipment):
    @classmethod
    def info(cls, model, price, year):
        cls.model = model
        cls.price = price
        cls.year = year
        return (
            f"подлежит размещению на складе принтер: модель:{cls.model}, стоимость:{cls.price}, год выпуска:{cls.year}\n")


class Scanner(Office_equipment):
    @classmethod
    def info(cls, model, price, year):
        cls.model = model
        cls.price = price
        cls.year = year
        return (
            f"подлежит размещению на складе сканнер: модель:{cls.model}, стоимость:{cls.price}, год выпуска:{cls.year}\n")


class Xerox(Office_equipment):
    @classmethod
    def info(cls, model, price, year):
        cls.model = model
        cls.price = price
        cls.year = year
        return (
            f"подлежит размещению на складе ксерокс: модель:{cls.model}, стоимость:{cls.price}, год выпуска:{cls.year}\n")


class Wrong_format(ValueError):
    pass


class Stock:
    max_count: int

    def __init__(self, count=0):
        self.max_count = count

    def store(self, value: int, value1: int, value2: int):
        self.value = value
        self.value1 = value1
        self.value2 = value2
        listKeys = ["Printers", "Scanners", "Xeroxes"]
        rez = {listKeys[0]: value, listKeys[1]: value1, listKeys[2]: value2}
        print(f"Итого на складе: {rez}")

    def shipment(self, quantity_of_shipped_goods: list):
        self.quantity_of_shipped_goods = quantity_of_shipped_goods


quantity_of_shipped_goods = []
while True:
    try:
        element = input(f"введите количество единиц техники на отгрузку/пробел чтобы закончить ввод")
        if element == " ":
            break
        if not element.isdigit():
            raise Wrong_format(element)
        quantity_of_shipped_goods.append(int(element))
    except Wrong_format:
        print('формат нечисловой')
print(quantity_of_shipped_goods)

example = ("samsung", 10000, 2009)
print(Printer.info("samsung", 10000, 2009))
example1 = ("sony", 20000, 2020)
print(Scanner.info("sony", 20000, 2020))
example3 = ("Kyocera", 9000, 2008)
print(Xerox.info("Kyocera", 9000, 2008))

a = Stock()
a.store((int(input(f"Введите количество принтеров на складе"))),
        (int(input(f"Введите количество сканнеров на складе"))),
        (int(input(f"Введите количество ксероксов на складе"))))
