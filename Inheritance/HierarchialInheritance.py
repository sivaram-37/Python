class Demo1:
    def __init__(self):
        self.x=100
    def test1(self):
        print("Inside the test1 method")
class Demo2(Demo1):
    def __init__(self):
        self.y=10
    def test2():
        print("Inside the test2 method")
    
class Demo3(Demo1):
    def __init__(self):
        self.z=600

d3=Demo3()
#print(d3.x)
d3.test1()
d2=Demo2()
#print(d2.x)
print(d2.y)