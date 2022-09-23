class Cat():
    name, color, weight = "", "", 0
    def meow(self):
        print(f"{self.name} говорит 'мяу'")

cat = Cat()
cat.name = "egor"
cat.color = "ginger"
cat.weight = "100000"
cat.meow()