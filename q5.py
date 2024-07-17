class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Test the program

# Create a Dog instance
dog = Dog()
print(f"Dog says: {dog.make_sound()}")

# Create a Cat instance
cat = Cat()
print(f"Cat says: {cat.make_sound()}")
