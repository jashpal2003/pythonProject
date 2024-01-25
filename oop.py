class animal:
    def eat(self):
        print("animal is now eating")
    def sleep(self):
        print("animal is sleeping ")
class dog:
    def bark(self):
        print("dog is barking ")
an = animal()
d = dog()
d.bark()
an.eat()