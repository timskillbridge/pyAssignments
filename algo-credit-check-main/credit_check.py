def credit_check(start):
    double = list(start[::-2])
    single = list(start[-2:0:-2])
    single.append(start[0])

    double1 = [int(x) for x in double]
    double2 = [sum(int(y) for y in str(int(x)*2)) \
    for x in single]
    total = sum(int(x) for x in double2+double1)

    if (total%10)==0:
        return "The number is valid!"
    else:
        return "The number is invalid!"

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

