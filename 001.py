"""
	Multiples of 3 and 5
"""
def mulgen(n):
    mul3 = []
    for i in range(n):    
        if i%3 == 0 or i%5 == 0:
            mul3.append(i)
    return sum(mul3)

mulgen(1000)
