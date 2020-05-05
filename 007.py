#%%
def isPrime(n):
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True
    if (n % 2 == 0 or n % 3 == 0): 
        return False
    i = 5
    while(i * i <= n) : 
        if (n%i == 0 or n%(i+2)==0) : 
          return False
        i = i + 6
    return True

def nthPrime(n):
    pList = []
    i = 0
    while True:
        if isPrime(i):
            pList.append(i)
            i+=1
        else:
            i+=1
        if(len(pList) == (n)):
            return pList[-1]

nthPrime(10001)


# %%
