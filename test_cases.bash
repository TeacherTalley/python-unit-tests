#!/bin/bash
# This script runs the test cases for the dog module using unittest and pytest.
python -m unittest dog test_dog.TestDog.test_bark_method
python -m unittest dog test_dog.TestDog.test_sit_method
# Run all tests in the dog module
python -m pytest
