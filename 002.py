def fibonacci_sum(n):
    fser = [0,1]
    while(True):
        if((fser[-1] + fser[-2])>n):
            break
        else:
            fser.append((fser[-2] + fser[-1]))
    evensum = 0
    for i in range(len(fser)):
        if(fser[i]%2 == 0):
            evensum = evensum + fser[i]
    return evensum
fibonacci_sum(4000000)
