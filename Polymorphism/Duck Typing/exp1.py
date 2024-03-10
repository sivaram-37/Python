class Calculator:
    def calculate(self,a,b):
        pass
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
    
def permit(ref,a,b):
    ref.calculate(a,b)
def main():
    permit(Add(),20,10)
    permit(Sub(),20,10)
main()