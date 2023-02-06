def kangaroo(x1, v1, x2, v2):
    # Write your code here
    prolly = False
    while True:
        if x1 == x2:
            prolly = True
            break
        
        if (v1 > v2 and x1 > x2) or (v2 > v1 and x2 > x1) or (v2 == v1 and x2 != x1):
            break
        x1 += v1
        x2 += v2
        
    if prolly:
        return 'YES'
    else:
        return "NO"