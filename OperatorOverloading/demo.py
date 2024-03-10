class Demo1:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name

d1=Demo1('Akash')
d2=Demo1(' Sharma')
print(d1+d2)