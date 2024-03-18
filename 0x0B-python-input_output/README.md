# 0x0B-python-input_output
This directory tests understanding of the following:
- file objects
- reading from and writing to files
- JSON encoder and decoder
1. **0-read_file.py** - `Python` function that reads a text file `(UTF8)` and prints it to stdout.
2. **1-write_file.py** - `Python` function that writes a string to a text file `(UTF8)` and returns the number of characters written.
3. **2-append_write.py** - `Python` function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
4. **3-to_json_string.py** - `Python` function that returns the `JSON` representation(string) of an object.
5. **4-from_json_string.py** - `Python` function that returns an object (Python data structure) from its `JSON` string.
6. **5-save_to_json_file.py** - `Python` function that writes an object to a text file, using its `JSON` representation.
7. **6-load_from_json_file.py** - `Python` function that creates an object from a `JSON` file.
8. **7-add_item.py** - `Python` script that adds all arguments to a list, and then save the JSON representation of the list to a file `add_item.json`.
9. **8-class_to_json.py** - `Python` function that returns the dictionary representation of an object. All attributes of the object's class are serializable: list, dictionary, string, integer and boolean.
10. **9-student.py** - Defines a class `Student`. It instantiates with public instance attributes `first_name`, `last_name` and `age`. It includes a public instance method `to_json` that returns the dictionary representation of a `Student` instance.
11. **10-student.py** - Updates the `Student` class by including an argument `attrs` to the `to_json` method. If `attrs` is a list of strings, only attribute names contained in this list must be retrieved otherwise, all attributes must be retrieved.
12. **11-student.py** - Updates `Student` class with a public method `reload_from_json` that takes in the dictionary representation of a student instance as argument. It uses this dictionary to update the values of the attributes of the instance.
