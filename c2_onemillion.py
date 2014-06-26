# Challenge: Write 1,000,000 as the product of two numbers;
# neither of which contains any zeroes.

def get_valid_numbers(maximum = 500000, bad = '0'):
    for i in range(maximum):
        if bad in str(i):
            continue
        yield i

for x in get_valid_numbers():
    for y in get_valid_numbers():
        if x * y == 1000000:
            print x, y
            exit()
        
        
        