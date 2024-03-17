# 0x0A-python-inheritance
This directory tests understanding of inheritance in `Python`.
1. **0-lookup.py** - `Python` function that returns the list of available attributes and methods of an object.
2. **1-my_list.py** - Definition of class `MyList` that inherits from `list`. It also includes a public instance method `print_sorted` that prints the list of integers in an ascending sort manner.
3. **tests/1-my_list.txt** - doctests for the MyList `class`.
4. **2-is_same_class.py** - `Python` function that returns `True` if the object is exactly an instance of the specified class otherwise `False`.
5. **3-is_kind_of_class.py** - Python function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from the specified class otherwise `False`.
6. **4-inherits_from.py** - `Python` function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class otherwise `False`.
7. **5-base_geometry.py** -  Defines an empty class `BaseGeometry`.
8. **6-base_geometry.py** - Update `BaseGeometry` with public instance method `area` that raises an exception saying area is not implemented.
9. **7-base_geometry.py** - Update `BaseGeometry` with public instance method `integer_validator` that validates if the value passed is an integer and greater than 0.
10. **tests/7-base_geometry.txt** - doctests for the `integer_validator` method.
11. **8-rectangle.py** - Defines `Rectangle` class that inherits from `BaseGeometry`. It instantiates private attributes `width` and `height` with width and height variables. It validates width and height with `integer_validator`.
12. **9-rectangle.py** - Updates `Rectangle` class by implementing the `area` method. It also defines `__str__` to give rectangle objects of `[Rectangle] <width>/<height>`.
13. **10-square.py** - Defines class `Square` that inherits from `Rectangle`. It instantiates with private instance attribute `size`. The size is validated with `integer_validator`. `Area` method is also implemented.
14. **11-square.py** - Updates `Square` class by defining `__str__` to give square description `[Square] <width>/<height>`.
