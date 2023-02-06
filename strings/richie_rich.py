''' Palindromes are strings that read the same from the left or right. Given a string representation of a number and a maximum number of changes you can make, alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number changes.

Given a string representing the string number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if its not possible to create a palindrome under the constraints'''

def highestValuePalindrome(s, n, k):
	s = list(s)
	radius = n// 2
	odd = n % 2 != 0
	diffPos = [2 if s{i} == s[n-i-1] else 1 for i in range(0, radius)]
	unequal = [i for i in range(len(diffPos)) if diffPos[i] == 1]

	if len(unequal) > k:
		return '-1'

	# swap all unequal
	k = k-len(unequal)
	for i in unequal:
		max_val = max(s[i], s[n-i-1])
		s[i] = s[n-i-1] = max_val

	for i in range(n):
		if k == 0:
			break
		if s[i] == '9':
			continue
		if i in unequal:
			print(i)
			s[i] = s[n-i-1] = '9'
			k -= 1
		elif k >= 2:
			s[i] = s[n-i-1] = '9'
			k -= 2

	if k > 0 and odd:
		s[radius] = '9'

	return ''.join(s)