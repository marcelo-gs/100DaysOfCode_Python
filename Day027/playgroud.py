def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3))
print(add(1,2,3,4, 5,6, 7,8, 9, 29))

def calculate(n,**kwargs):
    # for key,value in kwargs.items():
    #   print(key)
    #   print(value)
    n += kwargs["add"]
    n *= kwargs['multiply']
    return n

print(calculate(2, add=4, multiply=3))


class Car:

    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get('model')
        self.color = kw.get("color")


car = Car(make="Nissan", model="GT-R")
print(car.make)
print(car.model)
print(car.color)
