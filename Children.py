from Oops_demo import Calculator

class Childimplementation(Calculator):
    num2 = 200

    def __init__(self): #in child constructor declare parent constructor if default constructor is not declared
        Calculator.__init__(self,5,10)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


childobj = Childimplementation()
print(childobj.getCompleteData())


