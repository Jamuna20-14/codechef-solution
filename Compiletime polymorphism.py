class Calculator:
    def add(self, a, b=0, c=0):
    
print("Sum =", a + b + c)

obj = Calculator()

obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)

o/p:
Sum = 10
Sum = 30
Sum = 60
