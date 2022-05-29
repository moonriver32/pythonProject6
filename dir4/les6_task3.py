class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, wage, bonus):
        super().__init__(name, surname, wage, bonus)

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(int(self._income.get("wage")) + int(self._income.get("bonus")))


employee1 = Position("Ivan", "Ivanov", 10000, 5000)
employee1.get_full_name()
employee1.get_total_income()
employee2 = Position("Petr", "Petrov", 20000, 2000)
employee2.get_full_name()
employee2.get_total_income()
