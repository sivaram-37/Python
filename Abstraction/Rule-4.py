from abc import ABC,abstractmethod

class Student(ABC):
    def study(self):
        print("Study method")
    @abstractmethod
    def book(self):
        pass
class Child(Student):
    pass
c=Child() #Error
c.study()