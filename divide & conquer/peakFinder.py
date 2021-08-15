
def peakfinder_1D(a,st,sp):
    q=(sp+st)//2
    if a[q]<a[q-1]:
        return peakfinder_1D(a,st,q-1)
    else:
        if a[q]<a[q+1]:
            return peakfinder_1D(a,q+1,sp)
        else :
            return q,a[q]

def index_max(a):
    max_idx=0
    for i in range(len(a)):
        if a[i]>a[max_idx]:
            max_idx=i
    return max_idx

def peakfinder_2D(a,st,sp):
    n,m=a.shape
    q=(sp+st)//2
    max_idx=index_max(a[:,q])
    #max_idx,_=peakfinder_1D(a[:,q],0,n-1)
    #print(q)
    #print(max_idx)
    if q==0 or q==m-1:
        return a[max_idx,q]

    if a[max_idx,q]<a[max_idx,q-1]:
        return peakfinder_2D(a,st,q-1)
    else:
        if a[max_idx,q]<a[max_idx,q+1]:
            return peakfinder_2D(a,q+1,sp)
        else:
            return a[max_idx,q]