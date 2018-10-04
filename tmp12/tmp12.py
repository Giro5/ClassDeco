class Car:
    def __init__(self, **args):
        self.weight = args["wei"]
        self.color = args["col"]
        self.model = args["mod"]
        self.wheel = args["whe"]
    def Color(self):
        return self.color
    def Weight(self):
        return self.weight
    def Model(self):
        return self.model
    def Wheel(self):
        return self.wheel
    def Params(self):
        return self.color + " " + str(self.weight) + " " + self.model + " " + str(self.wheel)

car = Car(wei=1000, col="blue", mod="volvo", whe=4)
print(car.Color(), car.Model(), car.Weight(), car.Wheel())
print(car.Params())