# %%
import numpy as np
def isPal(n):
    n = str(n)
    nl = list(n)
    if nl == nl[::-1]:
        return True
    return False

def genpal(n):
    a = np.arange((10**n)-1,1,-1)
    b = np.arange((10**n)-1,1,-1)
    for i in range(len(a)):
        for j in range(len(b)):
            if isPal(a[i]*b[j]):
                return a[i]*b[j]

genpal(3)
#This doesnt seem to work for digits beyond 4, probably should fiddle with the range a bit...

# %%
