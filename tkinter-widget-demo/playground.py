# -----------------------------
# Programe by Vadim V.
#
# 
# Version     Date    Info
# 1.0         2020    Initial Version
# 
# -----------------------------
def add(*args):
    result = 0
    print(args)
    for arg in args:
        result += arg
    return result


print(add(1, 2, 3, 4, 5, 6))


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan", model="GT-R", seat=4)
print(my_car.make)
