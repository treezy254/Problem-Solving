def plusMinus(arr):
    # Write your code here
    total = len(arr)
    array = sorted(arr)
    positive = 0
    zero = 0
    negative = 0
    
    for i in array:
        if i > 0:
            positive += 1
            
        elif i == 0:
            zero += 1
            
        else:
            negative += 1
            
    pp = positive/total
    zp = zero/total 
    np = negative/total 
    
    rpp = f'{pp:.6f}'
    rzp = f'{zp:.6f}'
    rnp = f'{np:.6f}'