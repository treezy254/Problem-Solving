''' 
Given an amount and the denominations of coins available, determine how many ways change can be made for amount. There is a limitless supply of each coin type.
'''

def getWays(n, c):
    # Write your code here
    memo = {}
    return getWaysRec(n, c, 0, memo)

def getWaysRec(n, c, currentCoin, memo):
    if (n, currentCoin) in memo:
        return memo[n, currentCoin]
    if n== 0:
        return 1
    if n < 0:
        return 0
    
    nCombos = 0
    for i in range(currentCoin, len(c)):
        nCombos += getWaysRec(n - c[i], c, i, memo)
        
    memo[n, currentCoin] = nCombos 
    # store the number  of combos that can be made from n using the current coin
    return memo[n, currentCoin]
