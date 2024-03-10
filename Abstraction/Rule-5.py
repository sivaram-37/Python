from abc import ABC,abstractmethod

class Student(ABC):
    def study(self):
        print("Study method")
    @abstractmethod
    def book(self):
        pass
    @abstractmethod
    def play(self):
        pass

class Child(Student):
    def book(self):
        print("Book method")
    def play(self):
        print("Play method")

c=Child()
c.study()
c.book()
c.play()