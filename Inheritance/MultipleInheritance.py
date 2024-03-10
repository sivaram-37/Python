class Demo1():
    def __init__(self):
        self.x=100
    def test(self):
        print("Inside the test() of Demo1")
class Demo2():
    def __init__(self):
        self.y=100
    # def test(self):
    #     print("Inside the test() of Demo2")
class Demo3(Demo2,Demo1):
    pass
d3=Demo3()
print(d3.y)
d3.test()
print(Demo3.mro())
