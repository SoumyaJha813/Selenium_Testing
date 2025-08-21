class Parent:
    def greet(self):
        print("hello from parent class")

class Child(Parent):
    def __init__(self, title): #parameterized constructor
        self.title = title

    def helloGreet(self):
        #return "hello from child class"
        super().greet()
        print("hello from child class")
        print(self.title)

c = Child("title: soumya")
c.helloGreet()
c.greet()