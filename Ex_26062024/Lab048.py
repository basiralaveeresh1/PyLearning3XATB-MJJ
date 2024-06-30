class Car:
    name = None
    make = None
    model = None

    def __init__(self,name,make,model):
        self.name = name
        self.make = make
        self.model = model

    def getCarName(self):
        print(f"Car Name: {self.name} and Car Make: {self.make} and Car Model {self.model}")

car1 = Car("Veeresh", "Tata", "Safari")

car1.getCarName()