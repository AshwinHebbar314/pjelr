#%%
def power(a,x):
    return a**x

# %%
%%timeit -n 10
import math
def sum_of_digits(A,X):
    n = list(str(power(A,X)))
    a = list(map(int, n))
    return sum(a)
    
sum_of_digits(2,1000)

# %%
