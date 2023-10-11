#!/usr/bin/python3
def best_score(a_dictionary):
    """find key with the biggest integer value
    Args:
        a_dictionary: dictionary input
    Returns:
        key with the biggest value
    """
    if isinstance(a_dictionary, dict):
        if len(a_dictionary) == 0:
            return None
        scores = [a_dictionary[key] for key in list(a_dictionary)]
        max_ = max(scores)
        for key in list(a_dictionary):
            if a_dictionary[key] == max_:
                return key
    return None
