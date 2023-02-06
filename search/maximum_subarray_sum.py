''' we define the following:
		A subarray of array a of length n is contigous segment from a[i]
		throgh a[j] where 0 < i < j < n.

		The sum of an array is the sum of its elemensts.

	Given an n element array of integers, a, and an integer, m, determine the
	maximum value of the sum of any of its subarrays module m.

	Function Description

Complete the maximumSum function in the editor below.

maximumSum has the following parameter(s):

long a[n]: the array to analyze
long m: the modulo divisor
Returns
- long: the maximum (subarray sum modulo )
	'''


import itertools
import bisect

def maximumSum(a, m):

	a = list(map(Lambda x:x%m, itertools.accumulate(a)))
	maxi = max(a)
	arr = []
	for i in a:
		bisect .insort(arr, i)
		if i!=arr[-1]:
			maxi = max(maxi, (i-arr[bisect.bisect_right(arr, i)])%m)
	return maxi