# Author: Fransiskus Agapa

# ===========================
# simple program to practice abstract method
# choose an object and certain output show
# ===========================

from abc import ABC, abstractmethod     # needs to be installed and imported to use the abstract method


class Vehicle:

    @abstractmethod                     # means class & method cannot be instantiated
    def create(self):
        print("A vehicle is created")

    @abstractmethod
    def use(self):
        print("A vehicle is used")

    @abstractmethod
    def stop(self):
        print("A vehicle is stopped")


class SpeedBoat(Vehicle):

    def create(self):                  # method needs to be overwritten
        print("A speed boat is created")

    def use(self):
        print("A speed boat is running")

    def stop(self):
        print("The speed boat is stopped")


class Bus(Vehicle):

    def create(self):
        print("A bus is created")

    def use(self):
        print("A bus is running")

    def stop(self):
        print("The bus is stopped")


print("\n== Create | Use | Stop - Vehicle ==")
print("1. Speed boat")
print("2. Bus")
print("e. Exit")
choice = input("choice: ").lower()        # make user input to lower case to make while-loop condition simpler

while choice != 'e':
    if choice == '1':
        print("\n[ Speed boat ]\n")
        speed_boat = SpeedBoat()
        speed_boat.create()
        speed_boat.use()
        speed_boat.stop()

    elif choice == '2':
        print("\n[ Bus ]\n")
        bus = Bus()
        bus.create()
        bus.use()
        bus.stop()

    else:
        print("\n[ Invalid choice ]")

    print("\n== Create | Use | Stop - Vehicle ==")
    print("1. Speed boat")
    print("2. Bus")
    print("e. Exit")
    choice = input("choice: ").lower()  # make user input to lower case to make while-loop condition simpler

print("\n== Exit Program ==")
