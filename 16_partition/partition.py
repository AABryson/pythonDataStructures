def partition(lst, fn):
    true_list = []
    false_list = []
    combined_lists = []

    for x in lst:
        if fn(x) == True:
            true_list.append(x)
        else:
            false_list.append(x)
    combined_lists.append(true_list)  
    combined_lists.append(false_list)  
    return combined_lists
        
def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el, str)


    


"""Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """