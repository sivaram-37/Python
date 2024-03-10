class Demo1:
    def __init__(self):
        self.__x=10
    def disp1(self):
        print("Accessing inside disp1 using self",self.__x)
        print("Accessing inside disp1 using d1",d1.__x)
d1=Demo1()
d1.disp1()
#print(d1.__x)
# Exception has occurred: AttributeError
# 'Demo1' object has no attribute '__x'
#   File "D:\Python Workspace\Access Modifiers\PrivateAccessModifier.py", line 9, in <module>
#     print(d1.__x)
#           ^^^^^^
# AttributeError: 'Demo1' object has no attribute '__x'

class Demo2(Demo1):
    def disp2(self):
        print("Inside disp2 cannot access the value of __x from disp1")
#       print("Accessing inside disp2 using self",self.__x)
# Exception has occurred: AttributeError
# 'Demo2' object has no attribute '_Demo2__x'
#   File "D:\Python Workspace\Access Modifiers\PrivateAccessModifier.py", line 19, in disp2
#     print("Accessing inside disp2 using self",self.__x)
#                                               ^^^^^^^^
#   File "D:\Python Workspace\Access Modifiers\PrivateAccessModifier.py", line 21, in <module>
#     d2.disp2()
# AttributeError: 'Demo2' object has no attribute '_Demo2__x'

d2=Demo2()
d2.disp2()