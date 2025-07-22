# test_dog.py
# This file contains unit tests for the Dog and Poodle classes.
# It uses the unittest framework to ensure that the classes behave as expected.
# This file should be run in an environment where the Dog and Poodle classes are defined.

import unittest
from dog import Dog
from poodle import Poodle


class TestDog(unittest.TestCase):
    """Test cases for the Dog class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.dog = Dog("Buddy", 3)
        self.young_dog = Dog("Puppy", 1)
        self.old_dog = Dog("Senior", 10)

    def test_dog_initialization(self):
        """Test that Dog objects are initialized correctly."""
        self.assertEqual(self.dog.name, "Buddy")
        self.assertEqual(self.dog.age, 3)
        self.assertFalse(self.dog.sitting)

    def test_dog_initialization_with_different_values(self):
        """Test Dog initialization with various name and age values."""
        dog_with_long_name = Dog("Very Long Dog Name", 5)
        self.assertEqual(dog_with_long_name.name, "Very Long Dog Name")
        self.assertEqual(dog_with_long_name.age, 5)

        zero_age_dog = Dog("Zero", 0)
        self.assertEqual(zero_age_dog.age, 0)

    def test_bark_method(self):
        """Test that the bark method returns the correct string."""
        expected_output = "Buddy says Woof!"
        self.assertEqual(self.dog.bark(), expected_output)

        # Test with different dog names
        self.assertEqual(self.young_dog.bark(), "Puppy says Woof!")
        self.assertEqual(self.old_dog.bark(), "Senior says Woof!")

    def test_sit_method(self):
        """Test that the sit method works correctly."""
        # Initially, dog should not be sitting
        self.assertFalse(self.dog.sitting)

        # After calling sit, dog should be sitting
        result = self.dog.sit()
        self.assertTrue(self.dog.sitting)
        self.assertEqual(result, "Buddy is now sitting.")

        # Calling sit again should still work
        result2 = self.dog.sit()
        self.assertTrue(self.dog.sitting)
        self.assertEqual(result2, "Buddy is now sitting.")

    def test_stand_method(self):
        """Test that the stand method works correctly."""
        # First, make the dog sit
        self.dog.sit()
        self.assertTrue(self.dog.sitting)

        # Then make the dog stand
        result = self.dog.stand()
        self.assertFalse(self.dog.sitting)
        self.assertEqual(result, "Buddy is now standing.")

        # Calling stand again should still work
        result2 = self.dog.stand()
        self.assertFalse(self.dog.sitting)
        self.assertEqual(result2, "Buddy is now standing.")

    def test_sit_stand_sequence(self):
        """Test a sequence of sit and stand operations."""
        # Start standing
        self.assertFalse(self.dog.sitting)

        # Sit
        self.dog.sit()
        self.assertTrue(self.dog.sitting)

        # Stand
        self.dog.stand()
        self.assertFalse(self.dog.sitting)

        # Sit again
        self.dog.sit()
        self.assertTrue(self.dog.sitting)

    def test_str_method(self):
        """Test the __str__ method."""
        expected_output = "Buddy is 3 years old."
        self.assertEqual(str(self.dog), expected_output)

        # Test with different dogs
        self.assertEqual(str(self.young_dog), "Puppy is 1 years old.")
        self.assertEqual(str(self.old_dog), "Senior is 10 years old.")

    def test_repr_method(self):
        """Test the __repr__ method."""
        expected_output = "Dog(name=Buddy, age=3)"
        self.assertEqual(repr(self.dog), expected_output)

        # Test with different dogs
        self.assertEqual(repr(self.young_dog), "Dog(name=Puppy, age=1)")
        self.assertEqual(repr(self.old_dog), "Dog(name=Senior, age=10)")

    def test_dog_attributes_are_mutable(self):
        """Test that dog attributes can be changed after initialization."""
        # Change name
        original_name = self.dog.name
        self.dog.name = "NewName"
        self.assertEqual(self.dog.name, "NewName")
        self.assertNotEqual(self.dog.name, original_name)

        # Change age
        original_age = self.dog.age
        self.dog.age = 5
        self.assertEqual(self.dog.age, 5)
        self.assertNotEqual(self.dog.age, original_age)

    def test_multiple_dog_instances(self):
        """Test that multiple Dog instances are independent."""
        dog1 = Dog("Rex", 4)
        dog2 = Dog("Max", 6)

        # Make one dog sit
        dog1.sit()

        # Verify they have independent states
        self.assertTrue(dog1.sitting)
        self.assertFalse(dog2.sitting)

        # Verify they have different attributes
        self.assertNotEqual(dog1.name, dog2.name)
        self.assertNotEqual(dog1.age, dog2.age)


class TestPoodle(unittest.TestCase):
    """Test cases for the Poodle class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.poodle = Poodle("Bella", 2, "white")
        self.black_poodle = Poodle("Shadow", 4, "black")

    def test_poodle_initialization(self):
        """Test that Poodle objects are initialized correctly."""
        self.assertEqual(self.poodle.name, "Bella")
        self.assertEqual(self.poodle.age, 2)
        self.assertEqual(self.poodle.coat_color, "white")
        self.assertFalse(self.poodle.sitting)

    def test_poodle_inherits_from_dog(self):
        """Test that Poodle inherits Dog methods."""
        # Test inherited bark method
        expected_bark = "Bella says Woof!"
        self.assertEqual(self.poodle.bark(), expected_bark)

        # Test inherited sit/stand methods
        self.poodle.sit()
        self.assertTrue(self.poodle.sitting)

        self.poodle.stand()
        self.assertFalse(self.poodle.sitting)

    def test_groom_method(self):
        """Test the Poodle-specific groom method."""
        expected_output = "Bella is being groomed. The coat color is white."
        self.assertEqual(self.poodle.groom(), expected_output)

        # Test with different coat color
        expected_black = "Shadow is being groomed. The coat color is black."
        self.assertEqual(self.black_poodle.groom(), expected_black)

    def test_poodle_str_method(self):
        """Test the overridden __str__ method in Poodle."""
        expected_output = "Bella is a white Poodle, 2 years old."
        self.assertEqual(str(self.poodle), expected_output)

        expected_black = "Shadow is a black Poodle, 4 years old."
        self.assertEqual(str(self.black_poodle), expected_black)

    def test_poodle_repr_method(self):
        """Test that Poodle uses Dog's __repr__ method."""
        expected_output = "Dog(name=Bella, age=2)"
        self.assertEqual(repr(self.poodle), expected_output)

    def test_poodle_is_instance_of_dog(self):
        """Test that Poodle is an instance of Dog."""
        self.assertIsInstance(self.poodle, Dog)
        self.assertIsInstance(self.poodle, Poodle)

    def test_poodle_coat_color_variations(self):
        """Test Poodle with various coat colors."""
        brown_poodle = Poodle("Cocoa", 3, "brown")
        self.assertEqual(brown_poodle.coat_color, "brown")

        grey_poodle = Poodle("Silver", 5, "grey")
        self.assertEqual(grey_poodle.coat_color, "grey")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions."""

    def test_empty_string_name(self):
        """Test Dog with empty string name."""
        dog = Dog("", 5)
        self.assertEqual(dog.name, "")
        self.assertEqual(dog.bark(), " says Woof!")

    def test_special_characters_in_name(self):
        """Test Dog with special characters in name."""
        dog = Dog("Mr. Woof-a-lot", 3)
        self.assertEqual(dog.bark(), "Mr. Woof-a-lot says Woof!")

    def test_negative_age(self):
        """Test Dog with negative age."""
        dog = Dog("TimeTraveler", -1)
        self.assertEqual(dog.age, -1)
        self.assertEqual(str(dog), "TimeTraveler is -1 years old.")

    def test_very_large_age(self):
        """Test Dog with very large age."""
        dog = Dog("Ancient", 1000)
        self.assertEqual(dog.age, 1000)
        self.assertEqual(str(dog), "Ancient is 1000 years old.")

    def test_numeric_name(self):
        """Test Dog with numeric name."""
        dog = Dog("123", 2)
        self.assertEqual(dog.name, "123")
        self.assertEqual(dog.bark(), "123 says Woof!")


if __name__ == '__main__':
    # Create a test suite with verbose output
    unittest.main(verbosity=2)
