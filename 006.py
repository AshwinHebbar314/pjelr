#%%

def sq_of_ap(a,d,n):
    return (int((n/2)*(2*a + (n-1)*d)))**2
#sq_of_ap(1,1,10)

def sum_of_sq(n):
    return int(n*(n+1)*(2*n+1) / 6)
#sum_of_gp(10)

def result(a,d,n):
    return sq_of_ap(a,d,n) - sum_of_sq(n)

result(1,1,100)


# %%
