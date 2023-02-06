def migratoryBirds(arr):
    # Write your code here
    return max(set(arr), key=arr.count)