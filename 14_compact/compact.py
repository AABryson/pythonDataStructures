def compact(lst):
    copy_list = lst.copy()
    for x in copy_list:
        if bool(x) == False:
            copy_list.remove(x)
    return copy_list
print(compact([0, 1, 2, '', [], False, (), None, 'All done']))

#had trouble with the above; here is there answer
#return [val for val in lst if val]

"""Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """