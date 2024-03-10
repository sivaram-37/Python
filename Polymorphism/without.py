class Calculator:
    def calculate(self,a,b):
        print("Calculate Result :-")
class Add(Calculator):
    def calculate(self, a, b):
        print("Addition = ",a+b)
class Sub(Calculator):
    def calculate(self, a, b):
        print("Subraction = ",a-b)
class Mul(Calculator):
    def calculate(self, a, b):
        print("Multiplication = ",a*b)
class Div(Calculator):
    def calculate(self, a, b):
        print("Divition = ",a/b)
    

res=Add()
res.calculate(int(input("Enter the first number = ")),int(input("Enter the second number = ")))    
res=Sub()
res.calculate(int(input("Enter the first number = ")),int(input("Enter the second number = ")))    
res=Mul()
res.calculate(int(input("Enter the first number = ")),int(input("Enter the second number = ")))    
res=Div()
res.calculate(int(input("Enter the first number = ")),int(input("Enter the second number = ")))    