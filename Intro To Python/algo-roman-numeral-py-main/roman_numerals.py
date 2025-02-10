def to_roman(num):
    #if not isinstance(num,int) or num <1:
    if num <1:
        return False
    arranged_roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    arranged_arabic = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = dict(zip(arranged_roman,arranged_arabic))

    running_num = int(num) # if it was an integer, now it's not
    converted = []
    
    for x in range(len(arranged_arabic)-1,-1,-1):
        if running_num - arranged_arabic[x] >= 0:
            while running_num - arranged_arabic[x] >= 0:
                running_num -= arranged_arabic[x]
                converted.append(arranged_roman[x])

    return "".join(converted)



print(to_roman(3))
print(to_roman(9))
print(to_roman(5.9))
print(to_roman(494))