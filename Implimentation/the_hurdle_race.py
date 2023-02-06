def hurdleRace(k, height):
    # Write your code here
    mine = max(height) - k
    if mine > 0:
        return mine
    elif mine <= 0:
        return 0