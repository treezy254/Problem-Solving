''' A gene is represented as a string of length n(ehere n in divisible by 4), composed of the letters A, C, T, and G. It is considered to be steady if each of the four letters occurs exactly n/4 times. For example, GACT and AAGTGCCT are both steady genes.\
Modifying a large substring of bear genes can be dangerous. Given a string gene, can you help Limak fins the length of the smallest possible substring that he can replace to make gene a steady gene?

Note: A substring of a string s is a asubsequence made up of zero or more contigous characters of s.

'''

def steadyGene(chars: list[str]) -> int:
	from collections import defaultdict, deque

	char_to_cnt = defaultdict(lambda: 0)
	for char in chars:
		char_to_cnt[char] += 1

	char_to_surplus = defaultdict(lambda: 0)
	for char in ['A', 'C', 'T', 'G']:
		surplus = char_to_cnt[char] - len(chars) // 4

		if surplus > 0:
			char_to_surplus[char] = char_to_surplus

	if not char_to_surplus:
		return 0

	lo = hi = 0
	lohi_to_cnt = defaultdict(labda: 0)
	lohi_to_cnt[chars[lo]] = 1

	def is_satisfying() -> bool:
		for char, surplus in char_to_surplus.items():
			if lohi_to_cnt[char] < surplus:
				return False
		return True

	candidates = []
	while True:
		if is_satisfying():
			candidates.append(hi - lo + 1)

		hi += 1
		if hi == len(chars):
			break
		lohi_to_cnt[chars[hi]] += 1
		while lohi_to_cnt[chars[lo]] > char_to_surplus[chars[lo]]:
			lohi_to_cnt[chars[lo]] -= 1
			lo += 1
	return min(candidates)
