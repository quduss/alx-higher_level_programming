# 0x08-python-more_classes
This directory tests further on the following:
- Object-oriented programming
- objects and classes.
- Attributes and Property
- public, protected, and private attribute
- magic methods like `__repr__` and `__str__`
- class methods and static methods
1. **0-rectangle.py** - an empty class `Rectangle` that defines a rectangle.
2. **1-rectangle.py** - Updates `Rectangle` class with private instance attributes width and height. It also includes property and setter for the width and height private attributes.
3. **2-rectangle.py** - Updates `Rectangle` class by defining public instance methods `area` and `perimeter`.
4. **3-rectangle.py** - Updates `Rectangle` class by defining __str__ to allow rectangle objects to have a string representation.
5. **4-rectangle.py** - Updates `Rectangle` class by defining __repr__ to recreate a new instance from the repr string representation of an existing object.
6. **5-rectangle.py** - Updates `Rectangle` class by defining __del__ to print `Bye rectangle...` when an instance is deleted.
7. **6-rectangle.py** - Updates `Rectangle` class with public class attribute `number_of_instances` that returns the number of instances that exists.
8. **7-rectangle.py** - Updates `Rectangle` class with public class attribute `print_symbol`. The value of `print_symbol` defaults to the `#` symbol and can be changed to any type. It is used to print the rectangle instance.
9. **8-rectangle.py** - Updates `Rectangle` class with static method `bigger_or_equal` that returns the bigger rectangle between two rectangles based on area.
10. **9-rectangle.py** - Updates `Rectangle` class with class method `square` that returns a new rectangle instance with equal width and height.
