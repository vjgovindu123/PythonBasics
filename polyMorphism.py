class Cat:
    def actions(self):
        print("cat says meow meow")
class Dog:
    def actions(self):
        super().actions()
        print("dog says bow bow")
class Lion:
    def actions(self):
        super().actions()
        print("lion says Hahmmm")
c=Cat()
c.actions()
d=Dog()
d.actions()
e=Lion()
e.actions()
