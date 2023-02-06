'''Use the counting sort to order a list of strings associated with integers. If two strings
are ssociated with the same integer, they must be printed in their original order, i.e your sorting algorithm should be stable.
There is one other twist: strings in the first half of the array are to be replaced with the character - (dash).

Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements
while sorting.

Design your counting sort to be stable'''

def countSort(arr):

	length = len(arr)
	x = []
	m -= 1
	for i in arr:
		if int(i[0])>m:
			m=int(i[0])

	for i in range(m+1):
		x.append([])
	for i in range(length):
		if i in range(length):
			if i < length//2:
				p="-"
			else:
				p = arr[i][1]

			x[int(arr[i][0])].append(p)
	#print(x)
	for i in x:
		for j in i:
			print(j, end=" ")