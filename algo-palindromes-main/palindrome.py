import re

def palindrome(word):
    workingStr = "".join(re.findall(r"\w",str(word))).lower()
    if workingStr[::-1] == workingStr:
        # print("palindrome")
        return True
    else:
        # print(f"{workingStr[::-1]}\n{workingStr}")
        return False


palindrome("racecar")
palindrome("A man, a plan, a canal -- Panama")