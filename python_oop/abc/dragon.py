#!/usr/bin/env python3

"""Module dragon
Class dragon that inherits from both mixins classes"""

class SwimMixin():
    def swim(self):
        print("The creature swims!")

class FlyMixin():
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

toothless = Dragon()

toothless.swim()
toothless.fly()
toothless.roar()
