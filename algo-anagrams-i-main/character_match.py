# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	list0 = [0]
	str1 = string1.upper()
	str2 = string2.upper()
	dict1 = dict(zip(str1,list0*99))
	# dict1["space"] = 0
	dict2 = dict(zip(str2,list0*99))
	# dict2["space"] = 0

	for x,y in enumerate(str1):
		if y != ' ':
			if dict1.get(y,-1) != -1:
				dict1[y] +=1

	for x,y in enumerate(str2):
		if y != ' ':
			if dict2.get(y,-1) != y:
				dict2[y] += 1

	if dict1 == dict2:
		# print(f"{dict1}\n{dict2}")
		return True
	else:
		# print(f"{dict1}\n{dict2}")
		return False




# Part 2
def anagrams_for(word, list_of_words):
	answer = []
	for x,y in enumerate(list_of_words):
		if is_character_match(word,y):
			answer.append(y)
	# print(answer)
	return answer
