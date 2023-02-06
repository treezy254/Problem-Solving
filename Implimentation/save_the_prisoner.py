def saveThePrisoner(n, m, s):
    # Write your code here
    # n is number of prisoner
    # m is number of sweets
    # s is start position
    # if n is 7 and m is 19 then 19%7 = 5 start is 2 so 5 + 2 - 1 = 6
    # if n is 3 and m is 7 the 7%3 is 1 starrt is 3 so 3 + 1 - 1 = 3
    mod = m%n
    
    return (m + s -1) %n or n