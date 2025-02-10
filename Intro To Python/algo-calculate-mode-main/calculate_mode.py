def calculate_mode(numbers):
    testSet = list(set(numbers))
    highcount = []
    
    for x,y in enumerate(testSet):
        if len(highcount) == 0:
            highcount.append(y)
            # print(f"was empty so putting in {highcount[0]}")
        elif numbers.count(y) > numbers.count(highcount[0]):
                highcount = []
                highcount.append(y)
                # print(f"new high {highcount[0]}\n{highcount}")
        elif numbers.count(y) == numbers.count(highcount[0]):
                highcount.append(y)
                # print(f"adding {y} to {highcount[0]}\n{highcount}")
    return highcount
    
    
    





print(calculate_mode([1,2,3,3]))         # => [3]
print(calculate_mode([4.5, 0, 0]))       # => [0]
print(calculate_mode([1.5, -1, 1, 1.5])) # => [1.5]
print(calculate_mode([1,1,2,2]))         # => [1,2]
print(calculate_mode([1,2,3]))           # => [1,2,3], because all occur with equal frequency