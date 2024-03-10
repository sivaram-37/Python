class Demo1:
    def __init__(self):
        self.__x=10
    def disp1(self):
        print("Accessing inside disp1() using self :",self.__x)
        print("Accessing inside disp1() using d1 :",d1.__x)
d1=Demo1()
d1.disp1()
print("Accessing private variable using new name outside the class:",d1._Demo1__x)

class Demo2(Demo1):
    def disp2(self):
        print("Inside disp2() :- ")
        print("Accessing inside disp2() of child class Demo2 by using d1",d1._Demo1__x)
        print("Accessing inside disp2() of child class Demo2 by using d2",d2._Demo1__x)
d2=Demo2()
d2.disp2()

class Demo3:
    def disp3(self):
        print("accessing private variable inside another non child class : ",d1._Demo1__x)
d3=Demo3()
d3.disp3()