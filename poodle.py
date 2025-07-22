from dog import Dog
# In this example, we define a class `Dog` with an initializer method `__init__` that sets the dog's name and age.
# The `bark` method returns a string that includes the dog's name.
# We then create an instance of the `Dog` class called `my_dog` and call its `bark` method to print a message.
# Classes are a fundamental part of object-oriented programming in Python.
# They allow you to create complex data structures and encapsulate behavior related to those structures.
# You can create multiple instances of a class, each with its own attributes and methods.
# This promotes code reuse and organization, making it easier to manage larger programs.
# Classes can also inherit from other classes, allowing you to create a hierarchy of classes and share functionality.
# This is known as inheritance and is a key feature of object-oriented programming.
# In summary, classes in Python are a powerful way to define custom data types that can have both data and behavior.
# They help you organize your code, promote reuse, and enable the creation of complex data structures.
# Understanding classes is essential for writing object-oriented code in Python.

# make a Poodle class that inherits from Dog


class Poodle(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age)  # Call the initializer of the parent class
        self.coat_color = coat_color  # Additional attribute specific to Poodle

    def groom(self):
        return f"{self.name} is being groomed. The coat color is {self.coat_color}."

    def __str__(self):
        return f"{self.name} is a {self.coat_color} Poodle, {self.age} years old."


def main():
    # Example of creating an instance of the Poodle class
    my_poodle = Poodle("Bella", 2, "white")
    print(my_poodle.bark())  # Output: Bella says Woof!
    # Output: Bella is being groomed. The coat color is white.
    print(my_poodle.groom())
    print(my_poodle)  # Output: Bella is a white Poodle, 2 years old.


if __name__ == "__main__":
    main()
