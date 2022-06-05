class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("use pen")


class Pencil(Stationery):
    def draw(self):
        print("use pencil")


class Handle(Stationery):
    def draw(self):
        print("use handle")


draw_n = Stationery()
draw_n.draw()
draw_n1 = Pen()
draw_n1.draw()
draw_n2 = Pencil()
draw_n2.draw()
draw_n3 = Handle()
draw_n3.draw()
