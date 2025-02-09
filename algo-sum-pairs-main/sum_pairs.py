
def sum_pairs(numList,endGoal):
    checkList =  numList[:] #copy list contents and structure
    answerList = [] 
    pushTo = []
    for x,y in enumerate(numList): # cycle through the passed list of numbers, it will not be modified
        testNum = endGoal-y # look what number is needed to add to the current item in the passed list to equal the endGoal
        if testNum in checkList: # see if that number is in the list
            if testNum > y: 
                pushTo = [y,testNum]
            else:
                pushTo = [testNum,y]
            
            answerList.append(pushTo)
            checkList.pop(checkList.index(y))
            checkList.pop(checkList.index(testNum))
            # print(checkList)
    if len(answerList) >0:
        return answerList
    else:
        return "unable to find pairs"










print(sum_pairs([1,2,3,4,5], 9)) # [[4,5]]
print(sum_pairs([1,2,3,4,5], 7)) # [[2,5], [3,4]]
print(sum_pairs([3, 1, 5, 8, 2], 27)) # 'unable to find pairs'
print(sum_pairs([0,1,1,2,2,2,2,4,4,4,3,3,3,3,4,5,5,6,7,-1],6))