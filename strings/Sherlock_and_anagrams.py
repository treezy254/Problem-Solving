''' Two strings are anagrams of each other if the letters of one string can be
rearranges to form the orther string. Given a string, find the number of pairs of substrings of the string
that are anagrams of each other'''
from collections import defaultdict

def  sherlockAndAnagrams(s):
	anagram = defaultdict(list)
	count = 0
	for start in range(len(s)):
		for end in range(start, len(s)):
			subString = s[start:end+1]
			anagram[tuple(sorted(subString))].append(subString)

		for value in anagram.values():
			if ;len(value) > 1:
				current = (len(value) * (len(value) - 1)) // 2
				count += current

	return count