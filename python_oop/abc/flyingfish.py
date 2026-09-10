#!/usr/bin/env python3

"""Module flyingfish
Class FlyingFish that inherits from fish and bird class"""

class Fish():
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird():
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

magikarp = FlyingFish()

magikarp.fly()
magikarp.swim()
magikarp.habitat()

print(FlyingFish.mro())
