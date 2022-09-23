class Animal():
    def __init__(self, input_name):
        self.__pr_name = input_name
        print(f"Родилось животное {self.__pr_name} ")

    def eat(self):
        print("Намнём")
    def makeNoise(self):
        print(f"{self.__pr_name} говорит Гррр")

    def setName(self, new_name):
        self.__pr_name = new_name
    def getName(self):
        return self.__pr_name
    name = property(getName, setName)

class Cat():
    name, color, weight = "", "", 0
    def meow(self):
        print(f"{self.name} говорит 'мяу'")

class stringVar():
    def __init__(self, input_string):
        self.__pr_string = input_string

    def getString(self):
        return self.__pr_string
    def setString(self, input_string):
        self.__pr_string = input_string
    string = property(getString, setString)

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    def dist(self, p):
        from math import sqrt
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

p = Point(0, 0)
q = Point(1, 1)
print(p.dist(q))