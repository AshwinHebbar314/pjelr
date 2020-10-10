#%%
def collatz(x):
    counter = 0
    while(x!=1):
        counter += 1
        if(x%2 == 0):
            x = x/2
        else:
            x = (3*x + 1)
    return counter+1
#collatz(27)

#%%
import time
def determinelen(l):
    longlen = 0
    longind = 0
    for i in range(l, 0, -1):
        #if(i%100 == 0): 
        #   print("i = ", i)
        if(i%2 != 0):
            if(collatz(i) > longlen):
                longlen = collatz(i)
                longind = i            
    return longlen, longind
start = time.time()
print(determinelen(1000000))
end = time.time()
print(start)
print(end)
print(end-start)
# %%
