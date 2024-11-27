

class Animal:
    def speak(self):
        return "I am an animal."
    
    def rollover(self):
        print("I am rolling over")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof!"
    
    # def rollover(self):
    #     print("doggie roll")

dog = Dog()
animal = Animal()
print(animal.speak())  # Output: Woof!
print(dog.speak())  # Output: Woof!
dog.rollover()
animal.rollover()
