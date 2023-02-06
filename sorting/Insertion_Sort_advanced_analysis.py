''' Insertion sort is a simple sorting technique covered in previous challenges.
Sometimes, arrays may be too large for us to wait around for insertion sort to finish. Is there some other way
we can calculate the number of shifts an insertion sort performs when sorting an array?

if k[i] i sthe number of elements over which the ith elemnet of the arrays has to shift,
then the total number of shifts will be k[1] + k[2] +... + k[n] '''

def insertionSort(arr):
	len_arr = len(arr)

	if len_arr == 1:
		return 0

	mid = len_arr // 2
	n = len_arr - mid

	left = arr[:mid]
	right = arr[mid:]

	answer = insertionSort(left) + insertionSort(right)

	count_left = 0
	count_right = 0

	for i in range(len_arr):
		if count_left < mid and (count_right >= n or left[count_left] <= right[count_right]):
			arr[i] = left[count_left]
			answer += count_right
			count_left += 1

		elif count_right < n:
			arr[i] = right[count_right]
			count_right += 1
	return answer