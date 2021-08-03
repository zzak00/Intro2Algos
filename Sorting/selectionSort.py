def selectionSort(A):
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