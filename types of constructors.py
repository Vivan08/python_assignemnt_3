# creating a class student with parameterized constructor
class student :
    #parameterized constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f" Student name : {self.name} Student age : {self.age}")

    def display(self):
        print(f" Student name : {self.name} Student age : {self.age}")
# creating an object of the class student which invokes the parameterized constructor
s1 = student("abc",21)
# calling the display method to show student details
s1.display()