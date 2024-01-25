class animal:
    def eat(self):
        print("animal is now eating")
    def sleep(self):
        print("animal is sleeping ")
class dog(animal):
    def bark(self):
        print("dog is barking ")
    def sleep(self):
        print("dog is security ")
an = animal()
d = dog()
d.bark()
an.eat()
d.eat()