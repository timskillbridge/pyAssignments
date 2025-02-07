# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    answer = []
    for i,j in enumerate(numbers):
        
        tempList = [int(digit) for digit in str(j)]
        runningTotal = 0
        for items in tempList:
            runningTotal += int(items**len(tempList))
        if runningTotal == j:
            answer.append(runningTotal)
    return answer

# or 

def find_armstrong_numbers(numbers):
    answer = []
    for i,j in enumerate(numbers):
        
        tempList = [int(digit) for digit in str(j)]
        runningTotal = sum(map(lambda x: x**len(tempList),tempList))
        
        if runningTotal == j:
            answer.append(runningTotal)
    return answer

#print(find_armstrong_numbers([371,370]))

if __name__ == "__main__":
    pass

# done, two ways