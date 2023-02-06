def miniMaxSum(arr):
    # Write your code here
    job = sorted(arr)
    min = sum(job[:4])
    max = sum(job[1:])
    print(min, max)