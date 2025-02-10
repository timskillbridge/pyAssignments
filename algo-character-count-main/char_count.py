def char_count(str1):
    stripStr = str1.replace(" ","")
  # answer = sorted(\        Built this to return a sorted dictionary ... refactoring
  #   {char:str1.count(char)\
  #    for char in set(str1)}.items(),\
  #     key= lambda x:x[1], reverse=True)
    
    
    answer = []
    for x in set(stripStr):
        answer.append([x,stripStr.count(x)])
        
        
    return( sorted(answer, key= lambda x: (-x[1],x[0])) )

# # print(char_count("aaabbc"))

    # dict1 = {char:stripStr.count(char) for char in set(stripStr)}
    # list1 = (sorted([x, stripStr.count(x) for x in set(stripStr)], key = lambda x: (-x[1],x[0])))



    # print (dict1)
    # print(list1)

# print(char_count("an apple a day will keep the doctor away"))
# char_count()

