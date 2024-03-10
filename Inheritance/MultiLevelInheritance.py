class Demo1:
    def test1(self):
        print("Inside the test1 method")
class Demo2(Demo1):
    def test2(self):
        print("Inside the test2 method")
class Demo3(Demo2):
    def test3(self):
        print("Inside the test3 method")

d2=Demo2()
#d2.test3() // Error
d2.test2()

d3=Demo3()
d3.test1()
d3.test2()
d3.test3()