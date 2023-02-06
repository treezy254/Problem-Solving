import math 

def encryption(s):
    # Write your code here
    #remove spaces
    # find length and squre root of length and range of sqr
    # separate into colun=ms
    # add using indexing
    s = s.strip()
    cols = math.ceil(math.sqrt(len(s)))
    result = ''
    
    for i in range(0, cols):
        result += s[i]
        for j in range(cols + i, len(s), cols):
            result += s[j]
        result += " "
        
    return result
