def Insertion_Sort(A):
    for j in range(1,len(A)):
        key=A[j]
        # insert A[j] into the sorted sequence A[1:j]
        i=j-1
        while i>0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key    
    return A


def Selection_Sort(A):
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