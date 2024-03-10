class Demo1:
    def __init__(self):
        self._x=10
    def disp1(self):
        print("Accessing inside disp1 using self",self._x)
        print("Accessing inside disp1 using d1",d1._x)
d1=Demo1()
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print("Accessing inside disp2 using self",self._x)
d2=Demo2()
d2.disp2()