def twoPluses(grid):
    # Write your code here
    stack1 = []
    stack2 = []
    
    len1 = len(grid)
    len2 =len(grid[0])
    for i in range(1, len1-1):
        for j in range(1, len2-1):
            if grid[i][j] == 'G':
                sum1 = 1
                t = 1
                set1 = {(i, j)}
                stack1.append(sum1)
                stack2.append(set1)
                while i+t<= len1 - 1 and i-t >= 0 and j+t<= len2 - 1 and j-t>=0:
                    if grid[i+t][j] == 'G' and grid[i-t][j] == 'G' and grid[i][j+t] == 'G' and grid[i][j-t] == 'G':
                        set1.update({(i+t, j), (i-t,j), (i,j+t), (i,j-t)})
                        sum1+=4
                        t+=1
                        stack1.append(sum1)
                        stack2.append(set1.copy())
                    else:
                        break
    ans = -float('inf')
    for i in range(len(stack1)-1):
        for j in range(i+1, len(stack1)):
            if stack2[i].isdisjoint(stack2[j]):
                ans = max(ans, stack1[i]*stack1[j])
    return ans