# Challenge: Use the digits 0-9 to create two numbers. What is the highest 
# product you can achieve when these two numbers are multiplied together?

def permutes(s):
    if len(s) == 1:
        return [s]
    
    ret = []
    
    for i in range(len(s)):
        left = s[:i] + s[i+1:]
        for p in permutes(left):
            ret += [s[i] + p]
        ret += s[i]
    
    return ret
    
x = permutes('0123456789')
# this uses a lot of memory - there are a lot of permutations!






