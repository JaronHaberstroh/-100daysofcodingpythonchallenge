def calculate(n, **kwargs):
    for key, value in kwargs.items():
        # print(key)
        # print(value)
        n += kwargs["add"]
        n *= kwargs["multiply"]
        return n


print(calculate(2, multiply=5, add=3))


class Car():
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan", model="Altima-Hybrid")
print(my_car.model)
