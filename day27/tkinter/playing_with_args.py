def add(*args):
    total = 0
    for num in args:
        total += num
    print(total) 

add(1, 2, 3, 4)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)