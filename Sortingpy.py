
def insertion_sort(A):
    for j in range(1,len(A)):
        key=A[j]
        # insert A[j] into the sorted sequence A[1:j]
        i=j-1
        while i>0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key    
    return A


def selection_sort(A):
    for j in range(len(A)-1):
        min_index=j
        for i in range (j+1,len(A)):
            if A[i]<A[min_index]:
                min_index=i
        if min_index != j:
            temp=A[j]
            A[j]=A[min_index]
            A[min_index]=temp
    return A

def merge(A,p,q,r):
    # p: index start subarray 1
    # q: index start subarray 2
    L=A[p:q]
    R=A[q:r]
    L.append(float('inf'))
    R.append(float('inf'))
    i=0
    j=0
    for k in range(p,r):
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
    return A

def merge_sort(A,p,r):
    if p<r :
        q=(p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    return A

def bubbleSort(A): 
    n = len(A) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if A[j] > A[j+1] : 
                A[j], A[j+1] = A[j+1], A[j] 
    return A