from abc import ABC,abstractmethod

class Student(ABC):
    def study(self):
        print("Study method")
    @abstractmethod
    def book(self):
        pass
s=Student() #Error
s.study()