def getTotalX(a, b):
    # Write your code here
    ans = 0
    for i in range(1, 101):
        count = 0
        for x in a:
            if i % x == 0:
                count += 1
            if count == len(a):
                count = 0
                for y in b:
                    if y % i == 0:
                        count += 1
                    if count == len(b):
                        ans += 1
    return ans
            
    print(ans)