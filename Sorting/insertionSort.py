
def insertionSort(A):
    for j in range(1,len(A)):
        key=A[j]
        # insert A[j] into the sorted sequence A[1:j]
        i=j-1
        while i>0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key    
    return A
