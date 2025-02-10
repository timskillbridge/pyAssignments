def factorial(num):
	runningTotal = 1
	if num == 0 or num == 1:
		return 1
	elif isinstance(num,float):
		return False
	else:
		for x in range(num,1,-1):
			runningTotal *= x

	return runningTotal


# print(factorial(5))
# print(factorial(5.5))
# print(factorial(0))
# print(factorial(1))