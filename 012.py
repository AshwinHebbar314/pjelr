
#%%
def isEven(n):
    if n&1:
        return False
    else:
        return True

#%%
def Naturalsum(n):
    return n*(n+1)/2
Naturalsum(31)

#%%
def NoOfFactors(n):
    results = set()
    sqn = int(n**0.5)  ####NOT **2, ITS **0.5
    for i in range(1, sqn + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return len(results)
NoOfFactors(3800)
            

# %%
def TriangleNos(NoOfDivisors):
    n = 1
    while(True):
        ns = int(Naturalsum(n))
        if(isEven(ns)):
            #print(n, "Natural Sum: ", ns, "Factors", NoOfFactors(ns))
            if(NoOfFactors(ns) >= NoOfDivisors):
                return ns
        n += 1
TriangleNos(500)


# %%
