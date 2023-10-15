#!/usr/bin/python3
def weight_average(my_list=[]):
    """Calculate weighted average of integer tuples
    Args:
        my_list: list of integer tuples
    Return:
        weighted average of all integer tuples in list
    """
    sum_of_product = 0
    sum_of_weight = 0
    if len(my_list) == 0:
        return 0
    for tuple_ in my_list:
        sum_of_product += tuple_[0] * tuple_[1]
        sum_of_weight += tuple_[1]
    return sum_of_product / sum_of_weight
