'''Prof. Twotwo as the name suggests is very fond of powers of 2. Moreover he alse has a special affinity to number 800. He is known for carrying quirky experiments on powers of 2.
One day he played a game in his class. He broughts some number plates on each of which a digit from 0 to 9 is written. He made students stand in a row and gave a number plate to each 
of the students. Now turn by turn, he called for some tudents who are standing continously in the row say from index i to index j (i<=j) and asked them to find their strength.

The strength of the group of students from i to j is defined as:

strength(i, j)
{
	if a[i] = 0
		return 0; // if first child has value 0 in the group,
	value = 0
	for k fromi to j
		value = value* 10 + a[k]
	return value;
}

Prof called for all possible combinations of i and j and noted down the strength of each group. Now being interested in powers of 2, he wants to
find out how many strength are powers of two. Now its your responsibility to get the answer for prof.'''

tree = [False, {}]

def add(word) :
	current = tree
	for c in word:
		try:
			current = current[1][c]
		except KeyError:
			current[1][c] = [False, {}]
			current = current[1][c]
	current[0] = true

def count(word):
	count = 0
	for start in range(len(word)):
		current, index = tree, start
		while True:
			if current[0] :
				count += 1
			try :
				current = current[1][word[index]]
				index += 1
			except (KeyError, IndexError) :
				break
	return count

v = 1
for x in range(801) :
	add(str(v)[::-1])
	v <<= 1

Done = {}
T = int(input())
for t in range(T) :
	A = input()
	if not A in Done :
		Done[A] = count(A[::-1])
	print(Done[A])