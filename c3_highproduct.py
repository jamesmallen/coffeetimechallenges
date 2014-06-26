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
    
def whatsleft(s):
    ret = ''
    for i in range(10):
        if not str(i) in s:
            ret += str(i)
    
    return ret

ps1 = permutes('0123456789')
# this uses a lot of memory - there are a lot of permutations!

highest = 0
multiples = (0, 0)

for m1 in ps1:
    ps2 = permutes(whatsleft(m1))
    for m2 in ps2:
        m1 = int(m1)
        m2 = int(m2)
        if m1 * m2 > highest:
            multiples = m1, m2
            highest = m1 * m2
            print "%d * %d = %d" % (m1, m2, highest)




