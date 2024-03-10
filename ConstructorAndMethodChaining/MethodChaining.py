# Two ways to call method from child class
# Method-1:-
# class GreatGrandParent:
#     def cook(self):
#         print("GreatGrandParent is cooking Pulao")
# class GrandParent(GreatGrandParent):
#     def cook(self):
#         print("GrandParent is cooking Biryani")
#         super().cook()
# class Parent(GrandParent):
#     def cook(self):
#         print("Parent cooks dish")
#         super().cook()
# class Child(Parent):
#     def cook(self):
#         print("Child cooks Maggie")
#         super().cook()
# c=Child()
# c.cook()

# Method-2:-
class GreatGrandParent:
    def cook(self):
        print("GreatGrandParent is cooking Pulao")   
class GrandParent(GreatGrandParent):
    def cook(self):
        print("GrandParent is cooking Biryani")
class Parent(GrandParent):
    def cook(self):
        print("Parent cooks dish")
class Child(Parent):
    def cook(self):
        print("Child cooks Maggie")
        super().cook()
        super(Parent,self).cook()
        super(GrandParent,self).cook()
c=Child()
c.cook()