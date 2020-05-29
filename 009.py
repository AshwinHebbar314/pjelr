#%%
def genTriplets(z):
    a,b,c = 0,0,0
    for m in range(0,z):
        for n in range(0,m):
                a = ((m**2 - n**2))
                b = ((2*m*n))
                c = ((m**2 + n**2))
                if(a+b+c == 1000):
                    return a,b,c
genTriplets(500)



# %%
