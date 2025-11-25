# Creating a parent class named 'animal' with a method 'speak'
class animal:
    def speak(self):
        print("parent element animal speaking")
# Creating a child class named 'tiger' that inherits from 'animal' and overrides the 'speak' method
class tiger(animal):
    def speak(self):
        print("child element tiger speaking")
# Creating instances of both classes and calling their 'speak' methods
t = tiger()
a = animal()
# Calling the speak method on both instances
t.speak()
a.speak()