''' Given an array of integers and a terget value, determine the number of pairs of arrays elements
that have a difference equal to the target value.

Function Description

Complete the pairs function below.

pairs has the following parameter(s):

int k: an integer, the target difference
int arr[n]: an array of integers
'''

def pairs(k, arr):

	pairSet = set()
	arr.sort()
	counter = 0
	for val in arr:
		if val - k in pairSet:
			counter += 1
		pairSet.add(val)
	return counter