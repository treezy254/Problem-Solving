from collections import defaultdict

def nearlySimilarRectangles(sides):

    gcd = lambda a, b : (b , a % b) if b > 0 else a
    d = defaultdict(int)
    for l, w in sides:
        z = gcd(l, w)
        d[(l // z, w // z)] += 1

    return sum((x * (x - 1)) // 2 for x in d.values())
    

dope = [[5, 10], [10, 10], [3, 6], [9, 9]]

nearlySimilarRectangles(dope)