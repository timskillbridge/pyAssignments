def linear_search(value_to_find, array_to_search_through):
    for x in range(len(array_to_search_through)):
        if array_to_search_through[x] == value_to_find:
            return x

def linear_search_global(value_to_find, array_to_search_through):
    answerArr = []
    for x in range(len(array_to_search_through)):
        if array_to_search_through[x] == value_to_find:
            answerArr.append(x)
    if len(answerArr) >=1:
        return answerArr
    else: return False


# testArr = [1,5,7,9,12,17,12,6,9,84,76,2,55,12,4]
# testVal = 12
# print(linear_search(testVal,testArr))
# print(linear_search_global(testVal,testArr))