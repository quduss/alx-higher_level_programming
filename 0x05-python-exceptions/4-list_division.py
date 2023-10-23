#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for c in range(list_length):
        try:
            res = my_list_1[c] / my_list_2[c]
        except IndexError:
            print("out of range")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        finally:
            new_list.append(res)
    return new_list
