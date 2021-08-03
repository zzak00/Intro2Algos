def merge(A,p,q,r):
    # p: index start subarray 1
    # q: index start subarray 2
    # r: ending index subarray 2 (included)
    # A=[3,2,8,6,1]
    # mergeSort(A,0,4)
    L=A[p:q+1]
    R=A[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
    

def mergeSort(A,p,r):
    if p<r :
        q=(p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)