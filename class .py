class Car:
    def __init__(self, model1, model2, model3, model4):
        self.model01 = model1
        self.model02 = model2
        self.model03 = model3
        self.model04 = model4

    def BMW(self):
        pass

    def Audi(self):
        print(self.model01)


cars = Car("data1", "data2", "data3", "data4")

cars.BMW()
cars.Audi()

o/p:
data1
