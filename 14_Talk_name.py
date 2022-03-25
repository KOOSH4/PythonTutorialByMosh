class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi im {self.name}")


person1 = Person("Koosha")
print(person1.name)
person1.talk()

person2 = Person("TATA")
print(person2.name)
person2.talk()