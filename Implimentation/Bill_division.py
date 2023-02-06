def bonAppetit(bill, k, b):
    # Write your code here
    anna = (sum(bill)- bill[k])/2
    
    if anna == b:
        print("Bon Appetit")
    else:
        print(int(b - anna))