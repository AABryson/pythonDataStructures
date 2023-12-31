def find_the_duplicate(nums):
    duplicate_list = []
    for x in nums:
        for y in nums[:(nums.index(x)):-1]:
            if y == x: 
                duplicate_list.append(y)
                
    if duplicate_list != []:          
        return set(duplicate_list)
    else:
        return None
print(find_the_duplicate([1, 2, 1, 4, 3, 12]))
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))
print(find_the_duplicate([2, 1, 3, 4]) is None)



    # """Find duplicate number in nums.

    # Given a list of nums with, at most, one duplicate, return the duplicate.
    # If there is no duplicate, return None

    #     >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
    #     1

    #     >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
    #     9

    #     >>> find_the_duplicate([2, 1, 3, 4]) is None
    #     True
    # """
