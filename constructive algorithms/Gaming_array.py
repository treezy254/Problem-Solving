'''Andy wants to play a game with his little brother, Bob. The game starts with an array of distinct integers and the rules are as follows:

Bob always plays first.
In a single move, a player chooses the maximum element in the array. He removes it and all elements to its right. For example, if the starting array , then it becomes  after removing .
The two players alternate turns.
The last player who can make a move wins.
Andy and Bob play  games. Given the initial array for each game, find and print the name of the winner on a new line. If Andy wins, print ANDY; if Bob wins, print BOB.

To continue the example above, in the next move Andy will remove . Bob will then remove  and win because there are no more integers to remove.'''

def gamingArray(arr):
    # Write your code here
    curMax, maxesSoFar = arr[0], 1
    
    for idx in range(1, len(arr)):
        if curMax < arr[idx]:
            maxesSoFar += 1
            curMax = arr[idx]
            
    return 'ANDY' if maxesSoFar % 2 == 0 else 'BOB'
        
