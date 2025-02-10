
def isValid(s):
    validList =  [
        "(","[","{",")","]","}"
        ]
    openList = []
    closeList = []

    
    if s[0] not in validList[0:3]:
        return False
    for x, y in enumerate(s):
        if y in validList[0:3]:
            openList.append([y,x])
        else:
            closeList.append([y,x])
    # print(f"O-List:{openList}\nC-List:{closeList}")
    if len(openList) != len(closeList):
        return False
    
    for x,y in enumerate(openList):
        if s.count(y[0]) != s.count(validList[validList.index(y[0])+3]):
            print(f"y[0]: {s.count(y[0])} j:{s.count(validList[validList.index(y[0])+3])}")
            return False
            
        

    falseFlag = False
    for x,y in enumerate(openList):
        findMatch = validList[validList.index(y[0])+3]
        # print(f"{y[0]}{findMatch}")
        for i,j in enumerate(closeList):
            if j[0] == findMatch:
                if abs(i-x) == 1:
                    # print(f"Found it, {y[0]}{j[0]} {x}{i}")
                    falseFlag = False
                    continue
                elif abs(i-x)%3 == 0:
                    falseFlag = False
                    continue
                else:
                    # print(f"{y[0]}{j[0]}{x}{i}")
                    # print(startStr)
                    falseFlag = True
            # else:
            #     falseFlag = True
        
    if falseFlag == True:
        return False
    else:
        return True


#----My solution worked but this one was better and found on leetcode:---------------------
def isAlsoValid(s):
    # Initialize an empty stack and a hash map for matching brackets
    stack = []
    hash = {')': '(', ']': '[', '}': '{'}
    
    # Loop through each character in the string
    for char in s:
        if char in hash:
            # If it's a closing bracket, check the stack
            if stack and stack[-1] == hash[char]:
                stack.pop()  # Remove the matching opening bracket
            else:
                return False  # Invalid if no match
        else:
            # Push opening brackets onto the stack
            stack.append(char)
    
    # Return True if stack is empty, False otherwise
    return not stack
    



print(isValid("{}")==True)# should return true
print(isValid("(){}")==True)# should return true
print(isValid("({})")==True)# should return true
print(isValid("{[()]({})}()")==True)# should return true
print(isValid("(){}[])")==False) # should return false
print(isValid("][")==False) # should return false
print(isValid("(({}")==False) # should return false
print(isValid("())")==False) # should return false
print(isValid("}([]){")==False) # should return false
print(isValid("(]]") == False)

print("-")

print(isAlsoValid("{}")==True)# should return true
print(isAlsoValid("(){}")==True)# should return true
print(isAlsoValid("({})")==True)# should return true
print(isAlsoValid("{[()]({})}()")==True)# should return true
print(isAlsoValid("(){}[])")==False) # should return false
print(isAlsoValid("][")==False) # should return false
print(isAlsoValid("(({}")==False) # should return false
print(isAlsoValid("())")==False) # should return false
print(isAlsoValid("}([]){")==False) # should return false
print(isAlsoValid("(]]") == False)
