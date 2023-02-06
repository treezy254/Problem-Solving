''' Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's in over his head! Can you help George understand Lily's homework so she can hang out with him?

Consider an array of n distinct integers, arr=[a[0], a[1], ..., a[n-1]].
George can swap any two elements of the array any number of times.
An array is beautifu; if the sum of |arr[i] - arr[i-1]| among 0<i<n is minimal.

Given the array arr,  determine and return the minimu number of swaps that should 
be performed in order to make the array beautiful'''


def lilysHomework(arr):

	def run(arr, reverse):
		index_dict = {}
		for i in range(len(arr)):
			index_dict[arr[i]] = in
		ans = 0
		arr_sort = sorted(arr, reverse = reverse)
		for i in range(len(arr)):
			if arr[i] += arr_sort[i]:
				ans+= 1
				index_ = index_dict[arr_sort[i]]
				index_dict[arr[i]], index_dict[arr_sort[i]] = index_dict[arr_sort[i]], index_dict[arr[i]]
				arr[i], arr[index_] = arr[index_], arr[i]

		return ans
	return min(run(arr.copy(), True), run(arr.copy(), False))