def add(*args):
    total = 0
    for num in args:
        total += num
    print(total) 

# add(1, 2, 3, 4)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# calculate(2, add=3, multiply=5)

class Car: 
    def __init__(self, **kw):
        self.make=kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.year = kw.get("year")

my_car = Car(make="Nissan", model="GT-R", color="red")
print(my_car.year)