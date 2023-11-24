from collections import Counter

def freq_counter(coll):
    counts = {}
    for x in coll:
        counts[x] = counts.get(x, 0) + 1
    return counts

def same_frequency(num1, num2):
    num1 = str(num1)
    new_list = [int(n) for n in num1]
    first_counter = Counter(new_list)
    num2 = str(num2)
    second_list = [int(n) for n in num2]
    second_counter = Counter(second_list)
    

    return freq_counter(new_list) == freq_counter(second_list)
# print(num)
# num1 = list(num)
# print(num1)

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))

    # """Do these nums have same frequencies of digits?
    
    #     >>> same_frequency(551122, 221515)
    #     True
        
    #     >>> same_frequency(321142, 3212215)
    #     False
        
    #     >>> same_frequency(1212, 2211)
    #     True
    # """