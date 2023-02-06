def divisibleSumPairs(n, k, ar):
    # Write your code here
    mine = sorted(ar)
    ans = 0
    for i in range(len(ar)):
        for j in range (i + 1, len(ar)):
            if ((ar[i] + ar[j])%k == 0):
                ans += 1
                
    return ans