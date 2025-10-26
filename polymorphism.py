class Vehicle:
    def __init__(self, name):
        self.name = name
    
# --- Subclasses Demonstrating Polymorphism ---

class Car(Vehicle):
    def move(self):
        # Specific implementation for Car
        return f"{self.name} is driving along the road 🚗."

class Plane(Vehicle):
    def move(self):
        # Specific implementation for Plane
        return f"{self.name} is flying high above the clouds ✈️."

class Ship(Vehicle):
    def move(self):
        # Specific implementation for Ship
        return f"{self.name} is sailing across the open sea 🚢."
        
class Train(Vehicle):

    def move(self):
        # Specific implementation for Train
        return f"{self.name} is chugging along the tracks 🚂."


