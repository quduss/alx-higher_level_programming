# 0x0C-python-almost_a_circle
This Project tests understanding of the following:
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file
- args and kwargs
- Serialization/Deserialization
- JSON
1. **models/base.py** - Defines class `Base`. It instantiates with public instance attribute `id` and private class attribute `__nb_objects`. `__nb_objects` is set to 0 and increments when an object with an id of `none` is instantiated. This object's id becomes the value of `__nb_objects`.
2. **models/rectangle.py** - Defines class `Rectangle` that inherits from `Base`. It instantiates with private instance attributes `__width`, `__height`, `__x`, and `__y`. Each attributes has its public getters and setters. They are width, height, x and y respectively.
3. **models/rectangle.py** - Update the class `Rectangle` by adding validation of all setter methods and instantiation.
4. **models/rectangle.py** - Update the class `Rectangle` by adding the public method `area` that returns the area value of the Rectangle instance.
5. **models/rectangle.py** - Update the class `Rectangle` by adding the public method `display`. This method prints in stdout the Rectangle instance with the character `#`. `x` and `y` are not taken into account here.
6. **models/rectangle.py** - Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`.
7. **models/rectangle.py** - Improve the `display` method by taking care of `x` and `y`.
8. **models/rectangle.py** - Update the class `Rectangle` by adding the public method `update` that assigns each argument present in the `*args` to each attribute of the instance.
9. **models/rectangle.py** - Improve the `update` method by including `**kwargs` in the list of arguments to the method.
10. **models/square.py** - Defines class `Square` that inherits from `Rectangle`.
11. **models/square.py** - Update the class `Square` by adding the public getter and setter `size` to update and retrieve the size of the square.
12. **models/square.py** - Update the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns attributes of the instance with the values in `args` or `kwargs`.
13. **models/rectangle.py** - Update the class `Rectangle` by adding the public method `def to_dictionary(self)` that returns the dictionary representation of a `Rectangle` instance.
14. **models/square.py** - Update the class `Square` by adding the public method `def to_dictionary(self)` that returns the dictionary representation of a `Square` instance.
15. ****
