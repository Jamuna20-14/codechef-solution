class Car:
    def show(self):
        print("This is a car")

class BMW(Car):
    def show(self):
        print("This is BMW")

class Audi(Car):
    def show(self):
        print("This is Audi")

b = BMW()
a = Audi()

b.show()
a.show()

o/p:
This is BMW
This is Audi
