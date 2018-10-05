from random import *

class Car:
    def __init__(self, **args):
        self.weight = str(args["wei"])
        self.color = args["col"]
        self.model = args["mod"]
        self.price = str(args["pri"]) + " т.р."
    def Params(self):
        return "Color: " + self.color + "\nWeight: " + self.weight + "\nModel: " + self.model + "\nQuantity wheels: " + self.price

def decor(func):
    def picking(**args):
        return Car(**func(**args)).Params()
    return picking

@decor
def DefCar(**args):
    return args

models = ["volvo", "renault", "toyota", "audi", "bmw", "ford", "kia", "lexus", "mazda", "opel"]
for i in range(int(input("Укажите нужное кол-во машин: "))):
    value = DefCar(wei=randint(500, 2000), col="blue" if (i+1)%2==0 else "red", mod=choice(models), pri=randrange(500, 5000, 5))
    print(str(i+1)+"-я машина такова:\n" + value, "\n")