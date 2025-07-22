# Classes are a way to bundle data and functionality together.
# They allow you to create your own data types that can have both attributes (data) and methods (functions).
# Here's a simple example of a class in Python:
class Dog:
    # Constructor method to initialize the object
    # The __init__ method is called when an instance of the class is created.
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute
        self.sitting = False

    # bark method to simulate a dog's bark
    # Methods are functions defined within a class that operate on the instance of the class.
    def bark(self):      # Method
        return f"{self.name} says Woof!"

    # Write on your own
    def sit(self):
        self.sitting = True
        return f"{self.name} is now sitting."

    # Write on your own
    def stand(self):
        self.sitting = False
        return f"{self.name} is now standing."

    # String representation of the object
    def __repr__(self):
        return f"Dog(name={self.name}, age={self.age})"

    # This method is called when you use print on the object.
    def __str__(self):
        return f"{self.name} is {self.age} years old."


def main():
    # Example of creating an instance of the Dog class
    my_dog = Dog("Buddy", 3)
    print(my_dog.bark())  # Output: Buddy says Woof!

if __name__ == "__main__":
    main()