'''Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at index 1 in the string, and the remaining characters will ocur the same number of times. Given a string s, determine if its valid. If so, return YES, otherwise return NO '''

def isValid(s):
	chars = set(s)
	deletions = 0
	letters = {}

	for c in chars:
		letters[c] = s.count(c)

	val = list(letters.values())
	val_counter = Counter(val)
	common_value = val_counter.most_common(1)[0][0]

	for v in val:
		if common_value == v:
			continue

		elif v == 1:
			deletions += 1

		elif common_value - v not in [-1, 1]:
			deletions += 2
		else:
			deletions += 1

	return "YES" if deletions <= 1 else "NO"