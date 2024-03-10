class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        print(f"{self.name} is Working")
    def play(self):
        print(f"{self.name} is Playing")
        


emp1=Employee(input("Enter the name : "),int(input("Enter the age : ")))
emp2=Employee(input("Enter the name : "),int(input("Enter the age : ")))
print(emp1.name)
print(emp1.age)
emp1.work()
print(emp2.name)
print(emp2.age)
emp2.play()
