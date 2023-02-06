''' Consider a string, s of n lowercase English letters where each character,
si (0 < i<n), denotes the letter at index i in s. We define an(a,b,c,d)
palindromic tuple of s to be a sequence of indices in s satisfying the following creteria:

sa = sd, meaning the characters located at indies a and d are the same

sb = sc, meaning the charavters located at indices b and c are the same.

0 < a < b < c < d < |s|, meaning that a,b,c, and d are ascending in value and are valid indices withing string s.

Given s, find and print the number of (a, b, c, d) tuples satisfying the
above conditions. As this value can be quite large, print its module
(10^9 + 7).


Function Description
Complete the function shortPalindrome in the editor below.

shortPalindrome has the following paramter(s):
- string s: a string

Returns
- int: the number of tuples, modulo 
'''

def shortPalindrome(s):

	dim1 = [0] * 26
	dim2 = [0] * 26 * 26
	dim3 = [0] * 26

	count = 0

	mod = 1000000007

	for k in s:
		c = ord(k) - ord('a')

		count = (count + dim3[c]) % mod

		ic = c

		for i in range(26):

			dim3[i] = (dim3[i] + dim2[ic]) % mod
			dim2[ic] = (dim2[ic] + dim[i]) % mod
			ic += 26

		dim1[c] += 1

	return count