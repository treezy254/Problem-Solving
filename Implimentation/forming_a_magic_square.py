def formingMagicSquare(s):
    from itertools import permutations

    n = 3
    def ismagic(s):
        square = [s[r*n:r*n+n] for r in range(n)]
        
        if any(sum(s) != sum(r)*n for r in square):
            return False
        
        # diagnal elements
        square_D = [square[i][j] for i in range(n) for j in range(n) if i == j]
        
        if sum(s) != sum(square_D) * n:
            return False
        
        # transpose
        square_T = [[r[i] for r  in square] for i in range(n)]
        if any(sum(s) != sum(r)*n for r in square_T):
            return False
        # opposite diagonal
        square_D_O = [square[i][j] for i in range(n) for j in range(n) if i+j == n-1]
        if sum(s) != sum(square_D_O) * n:
            return 
        return True

    ## Permutates all posibilities distincts digits from 1 - 9
    all_magic_squares = [s for s in permutations(range(1, n**2 + 1)) if ismagic(s)]

    s = sum(s, []) # flatten s
    return min(sum(abs(x-y) for x, y in zip(s, ms)) for ms in all_magic_squares)
