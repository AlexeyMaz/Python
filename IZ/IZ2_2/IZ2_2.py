class Fraction:
    def __init__(self, *args):
        if len(args) == 2:
            self.integer = 0
            self.fr_up = args[0]
            self.fr_down = args[1]
        elif len(args) == 3:
            self.integer = args[0]
            self.fr_up = args[1]
            self.fr_down = args[2]
        else:
            print("А аргументы будут???")
            quit()

        if self.fr_down <= 0:
            self.fr_down = 1
            print("Теперь знаменатель = 1")

        if abs(self.fr_up) >= self.fr_down:
            self.integer += abs(self.fr_up) // self.fr_down
            if self.fr_up < 0:
                self.integer *= -1
            self.fr_up = abs(self.fr_up) % self.fr_down

    def __add__(self, other):
        if self.fr_down != other.fr_down:
            return Fraction(self.integer + other.integer,
                            self.fr_up * other.fr_down + other.fr_up * self.fr_down,
                            self.fr_down * other.fr_down)
        else:
            return Fraction(self.integer + other.integer,
                            self.fr_up + other.fr_up,
                            self.fr_down)

    def __sub__(self, other):
        if self.fr_down != other.fr_down:
            return Fraction(self.integer - other.integer,
                            self.fr_up * other.fr_down - other.fr_up * self.fr_down,
                            self.fr_down * other.fr_down)
        else:
            return Fraction(self.integer - other.integer,
                            self.fr_up - other.fr_up,
                            self.fr_down)

    def __mul__(self, other):
        return Fraction(0,
                        (self.fr_up + self.integer * self.fr_down) * (other.fr_up + other.integer * other.fr_down),
                        self.fr_down * other.fr_down)

    def __eq__(self, other):  # ==
        if self.fr_down != other.fr_down:
            return (self.integer * self.fr_down + self.fr_up) * other.fr_down == \
                   (other.integer * other.fr_down + other.fr_up) * self.fr_down
        else:
            return self.integer * self.fr_down + self.fr_up == \
                   other.integer * other.fr_down + other.fr_up

    def __ne__(self, other):  # !=
        return not self.__eq__(other)

    def __lt__(self, other):  # <
        if self.fr_down != other.fr_down:
            return (self.integer * self.fr_down + self.fr_up) * other.fr_down < \
                   (other.integer * other.fr_down + other.fr_up) * self.fr_down
        else:
            return self.integer * self.fr_down + self.fr_up < \
                   other.integer * other.fr_down + other.fr_up

    def __gt__(self, other):  # >
        return not self.__lt__(other) and self.__ne__(other)

    def __str__(self):
        if self.integer != 0 and self.fr_up != 0:
            return str(self.integer) + ' ' + str(self.fr_up) + '/' + str(self.fr_down)
        elif self.integer != 0 and self.fr_up == 0:
            return str(self.integer)
        elif self.integer == 0 and self.fr_up != 0:
            return str(self.fr_up) + '/' + str(self.fr_down)
        elif self.integer == 0 and self.fr_up == 0:
            return str(0)


f1 = Fraction(3, 4)
f2 = Fraction(1, 5, 9)
print(f1)
print(f2)
print(f"{f1} + {f2} = {f1 + f2}")
print(f"{f1} - {f2} = {f1 - f2}")
print(f"{f1} * {f2} = {f1 * f2}")
