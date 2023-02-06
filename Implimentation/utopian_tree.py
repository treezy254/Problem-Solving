def utopianTree(n):
    # Write your code here
    h = 1
    i = 0
    while i <= n:
        if i == 0:
            h = 1
            
        elif i%2 != 0:
            h *= 2
            
        elif i%2 == 0:
            h += 1
            
        i += 1
            
    return h