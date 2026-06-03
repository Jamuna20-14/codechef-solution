class Dad:
    def __init__(self):
        self.x = "Raja"

class Mom:
    def __init__(self):
        self.y = "Rani"

class Jodha(Dad, Mom):
    def __init__(self):
        Dad.__init__(self)
        Mom.__init__(self)

    def display(self):
        print("Dad Name :", self.x)
        print("Mom Name :", self.y)

obj = Jodha()
obj.display()

o/p:
Dad Name : Raja
Mom Name : Rani
