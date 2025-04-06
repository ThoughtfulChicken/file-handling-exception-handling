# polymorphism_challenge.py

class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("The dog runs!")

class Cat(Animal):
    def move(self):
        print("The cat jumps!")

class Bird(Animal):
    def move(self):
        print("The bird flies!")

# Create instances and test polymorphism
animals = [Dog(), Cat(), Bird()]

for animal in animals:
    animal.move()  # Polymorphism in action
