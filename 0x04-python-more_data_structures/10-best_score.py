#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    acu = list(a_dictionary.keys())[0]
    eam = a_dictionary[acu]
    for i, j in a_dictionary.items():
        if j > eam:
            eam = j
            acu = i
    return (acu)
