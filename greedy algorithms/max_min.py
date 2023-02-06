'''You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

Where:
- max denotes the largest integer in 
- min denotes the smallest integer in '''


def maxMin(k, arr):
    # Write your code here
    arr.sort()
    i = 0
    ans = arr[-1]
    while i+k<=len(arr):
        un = arr[i+k-1] - arr[i]
        if un<ans : ans = un
        i += 1
    return ans