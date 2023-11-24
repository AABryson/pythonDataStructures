def intersection(l1, l2):
    set_l1 = set(l1)
    set_l2 = set(l2)
    set_intersection = set_l1 & set_l2
    intersection_list = list(set_intersection)
    return intersection_list




"""Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """