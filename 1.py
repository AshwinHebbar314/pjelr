#%%
def mulgen(n):
    mul3 = []
    mul5 = []
    for i in range(n):    
        if(i%3 == 0):
            mul3.append(i)
        if(i%5 == 0):
            mul5.append(i)
    mulall = list(set(mul3 + mul5))
    return sum(mulall)
    

mulgen(10)


# %%
