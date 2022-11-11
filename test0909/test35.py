"""
抽象类
"""


class Animal:
    name: None

    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


cat = Cat()
dog = Dog()


def make_noise(animal: Animal):
    animal.speak()
    print("来点声音")


make_noise(cat)
make_noise(dog)


class AC:
    def make_cool(self):
        pass

    def make_hot(self):
        pass

    def make_l_r(self):
        pass


class Meidi(AC):
    def make_cool(self):
        print("美的空调制冷")

    def make_hot(self):
        print("美的空调制热")

    def make_l_r(self):
        print("美的空调左右摆风")


class Gree(AC):
    def make_cool(self):
        print("格力空调制冷")

    def make_hot(self):
        print("格力空调制热")

    def make_l_r(self):
        print("格力空调左右上下摇摆")


def make_cool(ac: AC):
    ac.make_cool()


meidi = Meidi()
gree = Gree()

make_cool(meidi)
make_cool(gree)
