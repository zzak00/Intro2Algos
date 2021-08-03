def maxHeapify(A,i):
    n= len(A)
    l= 2*i+1
    r= 2*i+2
    if l<n and A[l]>A[i]:
        larg=l 
    else:
        larg=i
    if r<n and A[r]>A[larg]:
        larg=r
    if larg!=i:
        A[i],A[larg]=A[larg],A[i]
        maxHeapify(A,larg)


def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        maxHeapify(A,k)

def HeapSort(A):
    D=[]
    build_max_heap(A)
    while len(A):
        A[-1],A[0]=A[-1],A[0]
        D.append(A.pop())
        maxHeapify(A,0)
    return D


