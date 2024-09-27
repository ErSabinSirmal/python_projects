
"""Unlimited positional Arguments"""
def add(*args):
    sum =0
    print(args[3])
    for n in args:
        sum += n
    return sum


print(add(1,2,3,4,5,6,7,8,9,10))


def calculate(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(add = 3, multiply = 5)

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = Car(make = "Toyota", model = "Supra")
print(my_car.model)