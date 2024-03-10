from abc import ABC,abstractmethod

class Student(ABC):
    def study(self):
        print("Study method")
s=Student()
s.study()