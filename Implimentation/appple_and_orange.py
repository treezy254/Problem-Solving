def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apps = []
    org = []
    ta = 0
    to = 0
    for i in apples:
        i += a
        apps.append(i)
        
    for i in oranges:
        i += b
        org.append(i)
    
    for i in apps:
        if i >= s and i <= t :
            ta += 1
            
    for i in org:
        if i >= s and i <=t:
            to += 1
            
    print(ta)
    print(to)