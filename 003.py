#%%
import numpy as np
def isEven(n):
    if n&1:
        return False
    else:
        return True

def isFactor(i,n):
  if n%i == 0:
    return True
  else:
    return False

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

def prime_factor(n):
  l1 = []
  for i in range(int(round(np.sqrt(n)))):
    if(i*i <= n):
      if isEven(i) == False and isPrime(i) and isFactor(i,n):
            l1.append(i)
  return np.max(l1)

prime_factor(600851475143)
