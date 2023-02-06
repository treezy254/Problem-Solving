''' In this challenge, Hannah provides a string s consisiting of lowercase English letters. Every day for q days, she would select two integers l and r, 
take the substring Sl...Sr( the substring of s from index l to index r), and ask the following question:

Consider all the palindromes that can be constructed from some of the letters Sl ...Sr. You can reorder the letters as you need. Some of these palindromes
have the maximum length among all these palindromes. How many maximum-length palindromes are there?
'''

def initialize(s):
	global arr, fac, mod, M
	M = 10000000007
	n = len(s)
	arr = [[0 for _ in range(n + 1)] for _ in range(26)]
	for i in range(n):
		for j in range(26):
			arr[j][i + 1] = arr[j][i] + ((ord(s[i]) - 97) == j)

		fac = [1] * (n + 1)
		mod = [1] * (n + 1)
		for i in range(1, n + 1):
			fac[i] = (fac[i - 1] * i) % mod
			mod[i] = pow(fac[i], M - 2, M)


def answerQuery(l, r):
	global arr, fac, mod, M
	odd = 0
	even = 0
	divs = 1
	for i in range(26):
		value = arr[i][r] - arr[i][l - 1]
		odd += (value & 1)
		even += (value // 2)
		divs = (divs * mod[value//2]) % mod
	result = (fac[even] * divs) % M
	if (odd > 0):
		result = (result * odd) % M 
	return result