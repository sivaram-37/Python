class Demo1:
    def __init__(self):
        self.x=100
    def test1(self):
        print("Inside the test1 method")
class Demo2(Demo1):
    pass
d2=Demo2()
d2.test1()
print(d2.x)