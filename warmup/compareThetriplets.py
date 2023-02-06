def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
            
        if a[i] < b[i]:
            bob += 1
            
    return [alice, bob]