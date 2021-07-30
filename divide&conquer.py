# Inversions
# A[1..n] is an array of n distinct numbers. if i<j and A[i]>A[j] then pair (i,j) is called an inversion of A
# Count inversions wit O(nlgn)
def inversionsBF(arr):
    num_inversions = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                num_inversions += 1

    return num_inversions

def mergeInv(A,p,q,r):
    global count
    # p: index start subarray 1
    # q: index start subarray 2
    # r: ending index subarray 2 (included)
    L=A[p:q+1]
    R=A[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i=j=0
    for k in range(p,r+1):
        if L[i]>R[j]:
            A[k]=R[j]
            j=j+1
            count+=len(L)-1
        else:
            A[k]=L.pop(0)

def count_inversions(A,p,r,count):
    if p<r :
        q=(p+r)//2
        count_inversions(A,p,q,count)
        count_inversions(A,q+1,r,count)
        mergeInv(A,p,q,r)

def main():
    a=[1,5,4,8,10,2,6,9,12,11,3,7]
    print("number of inversions brute force = ", inversionsBF(a))
    count_inversions(a,0,len(a)-1,count)
    print("number of inversions divide & conquer ",count)

if __name__ == "__main__":
    count=0
    main()
