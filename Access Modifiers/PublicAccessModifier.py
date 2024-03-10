class Demo1:
    def __init__(self):
        self.x=10
    def disp1(self):
        print("Accessing inside disp1 using self",self.x)
        print("Accessing inside disp1 using d1",d1.x)
d1=Demo1()
d1.disp1()
print("Accessing outside the class using d1",d1.x)

class Demo2(Demo1):
    def disp2(self):
        print("Accessing inside disp2 using self",self.x)
d2=Demo2()
d2.disp2()