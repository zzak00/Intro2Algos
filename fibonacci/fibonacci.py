import numpy as np

def fibonacci(n):
    if n < 2:
       return n
    else:
       return fibonacci(n-1)+fibonacci(n-2)

if __name__=='__main__':
    n=int(input('Please enter an integer --> '))
    while n<0:
        n=int(input('Please enter a positive integer --> '))
    print(fibonacci(n))

    ## golden ratio
    gr=(1+np.sqrt(5))/2
    print((1/np.sqrt(5))*(gr**n))

