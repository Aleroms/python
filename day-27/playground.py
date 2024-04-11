def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3))


# keyword arguments
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(3, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make, my_car.model)
