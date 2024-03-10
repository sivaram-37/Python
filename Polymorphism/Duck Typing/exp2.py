#Without Inheritance and Explanation
# 1)Three classes(Add,Sub and Mul) are defined.
# 2)The permit() takes an object reference and two numbers as input,calling the calculate() if available;
#otherwise,it notify the absence of the method.
# 3)In main(),instances of Add(),Sub() and Mul() are passed to permit,demonstating behaviour-based acceptance.

class Add:
    def calculate(self, a, b):
        print("Addition = ",a+b)
class Sub:
    def calculate(self, a, b):
        print("Subraction = ",a-b)
class Mul:
    pass

def permit(ref,a,b):
    if type(ref).__name__=='Mul':
        print("Mul does not have method - claculate()")
    else:
        ref.calculate(a,b)
def main():
    permit(Add(),20,10)
    permit(Sub(),20,10)
    permit(Mul(),20,10)
main()