# Challenge: Find three digits X, Y and Z such that
# XYZ in base10 is equal to ZYX in base9?

for i in range(1, 1000):
    s = "%03d" % (i)
    # x, y, z = s
    
    try:
        if int(s, 10) == int(s[::-1], 9):
            print s
    except:
        pass