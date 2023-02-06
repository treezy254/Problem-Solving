''' Samantha and Sam are playing a numbers game. Given a number as a string, no leading zeros, determine the sum of all integer values of substrings of the string.

Given an integer as a string, sum all of its substrings cast as integers. As the number may become large, return the value modulo .'''

def substrings(n):
	# Write your code here
	length = len(n)
	ans = 0
	mod = 10**9 + 7
	i = 0
	for ltt in n[::-1]:
		i = (10*(i%mod)+1)%mod
		lt = int(ltt)
		ans += (lt*i*length)%mod
		length -= 1
	return ans%mod