from dog import Dog
from cat import Cat
from mouse import Mouse
import pprint
# Get user input
animal_type = input("Enter the type of animal to create (Dog, Cat, Mouse): ").lower().capitalize()

# Dynamically create an instance of the class
try:
    # pprint.pprint(globals())
    animal_class = globals()[animal_type]  # Access the class by its name
    animal = animal_class()  # Create an instance
    print(f"Created a {animal_type}: {animal.jump()}")
except KeyError:
    print(f"Error: '{animal_type}' is not a valid animal type.")
except AttributeError:
    print(f"The animal {animal_type} is not able to do the jump action")
