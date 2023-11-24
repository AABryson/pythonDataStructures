def min_max_keys(d):
    keyss = d.keys()
    maxi = max(keyss)
    mini = min(keyss)
    return (mini, maxi)
    
print(min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))
print(min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"}))


    # """Return tuple (min-keys, max-keys) in d.

    #     >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
    #     (1, 10)

    # Works with any kind of key that can be compared, like strings:

    #     >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
    #     ('apple', 'cherry')
    # """