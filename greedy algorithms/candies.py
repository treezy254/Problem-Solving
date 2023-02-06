'''Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.'''

def candies(n, arr):
    # Write your code here
    x = sorted(enumerate(arr), key = lambda x: x[1])
    out = [0]*n
    for i, val in x:
        k1 = out[i - 1] if i and val > arr[i-1] else 0
        k2 = out[i+1] if i<n-1 and val > arr[i+1] else 0
        out[i] = max(k1, k2) + 1
    return sum(out)
    