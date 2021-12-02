class dlugosc:
    def __init__(self, dlugosc, jednostka = "m"):
        self.dlugosc = dlugosc
        self.jednostka = jednostka

    def __str__(self):
        return str(self.dlugosc) + " " + self.jednostka

    def convert_to_m(self):
        if self.jednostka == "mm":
            return self.dlugosc / 1000
        elif self.jednostka == "cm":
            return self.dlugosc / 100
        elif self.jednostka == "m":
            return self.dlugosc
        elif self.jednostka == "km":
            return self.dlugosc * 1000

    def __add__(self, other):
        return dlugosc(self.convert_to_m() + other.convert_to_m())

    def __sub__(self, other):
        return dlugosc(self.convert_to_m() - other.convert_to_m())

if __name__ == '__main__':
    x = dlugosc(2)
    y = dlugosc(4000, "mm")
    z = dlugosc(100, "cm")

    print("x = ", str(x))
    print("y = ", str(y))
    print("z = ", str(z))

    print("suma x + y + z =", str(x + y + z))
    print("suma x + y - z =", str(x + y - z))