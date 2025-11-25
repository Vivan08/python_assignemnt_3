Ans 1

Method Overloading (Simulated):
In Python, defining multiple methods with the same name results in overwriting, not overloading. To achieve the functional result of overloading—having one method name handle different scenarios—Python programmers rely on a single function definition utilizing default arguments or variable argument lists (*args, **kwargs). This allows the method to inspect the passed arguments at runtime and execute the appropriate logic, simulating the flexibility of traditional overloading.

Method Overriding (Standard):
Method overriding is a fully supported and standard feature in Python that relies on inheritance. A child class can provide its own implementation for a method that is already defined in its parent class. When the method is called on an instance of the child class, the child's implementation takes precedence. The super() function is commonly used within the child's overriding method to explicitly call and incorporate the behavior of the parent's original method, enabling code reuse and extension.

Ans 2

A constructor is a special method in a class that automatically runs when an object is created.
Its main purpose is to initialize object variables (also called instance attributes

1. Default Constructor

  A constructor with no arguments (except self)

  Used when there is nothing special to initialize


2. Parameterized Constructor

  A constructor that takes arguments

  Used to give different values to each object
