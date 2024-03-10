class Demo1():
    def __init__(self):
        self.x=100

class Demo2(Demo1):
    def __init__(self):
        self.y=200
        super().__init__()

d2=Demo2()
print(d2.y)
print(d2.x)
