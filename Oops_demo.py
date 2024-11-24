class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b

    def getData(self):
        print("I am now executing this getData Function.")

    def summation(self):
        return self.firstNum + self.secondNum + self.num


obj = Calculator(3, 6)
obj.getData()
print(obj.summation())
