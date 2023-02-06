'''Find the number of ways that a given integer, , can be expressed as the sum of the  powers of unique, natural numbers.

For example, if  and , we have to find all combinations of unique squares adding up to . The only solution is .

Function Description

Complete the powerSum function in the editor below. It should return an integer that represents the number of possible combinations.

powerSum has the following parameter(s):

X: the integer to sum to
N: the integer power to raise numbers to'''

def powerSum(X, N, a=1):
    # Write your code here
    if X < 0 or X < a**N:
        return 0
    if X == 0 or X == a**N:
        return 1
    return powerSum(X-a**N, N, a+1) + powerSum(X, N, a + 1)