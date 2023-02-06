from collections import Counter 

def nonDivisibleSubset(k, s):
    c = Counter([ss % k for ss in s])
    n = sum(max(c[i], c[k-i]) for i in range(1, k//2 + k%2))
    return n + (0 in c) + (k%2 == 0 and k/2 in c)

    # for i, j in range(s, 2v)