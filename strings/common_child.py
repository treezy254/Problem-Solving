''' a string is said to be a child of a another string if it can be formed by deleting
0 or more characters from the other string. Letters cannot be rearranged. Given two
strings of equal length, what's the longest string that can be constructed such that its a child
of both? '''

def commonChild(s1: str, s2: str) -> int:
	# Time Complexity O(x^2)
	max_at = {}
	for c1  in s1:
		current_max = 0
		for i, c2 in enumerate(s2):
			potential_sum = current_max + 1
			current_max = max(current_max, max_at.get(i, 0))
			if c1 == c2:
				max_at[i] = potential_sum

	return max(max_at.values(), default=0)