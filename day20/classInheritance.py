class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("breathing underwater")

    def swim(self):
        print("moving underwater")


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def run(self):
        print("moving really fast on land")

    def dig(self):
        print("digging in the ground")


nemo = Fish()
print(nemo.num_eyes)
nemo.breathe()
