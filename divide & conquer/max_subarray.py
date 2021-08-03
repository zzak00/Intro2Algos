# Maximum subarray problem

def find_max_crossing_subarray(A,low,mid,high):
    left_sum = -1*float('inf')
    max_left=mid
    sum = 0
    for i in range(mid,low+1,-1):
        sum+=A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -1*float('inf')
    max_right=mid
    sum = 0
    for j in range(mid+1,high+1):
        sum += A[j]
        if sum > right_sum :
            right_sum = sum
            max_right = j
    return max_left+1,max_right+1,left_sum+right_sum


def find_maximum_subarray(A,low,high):
    if high == low :
        return (low,high,A[low])
    else :
        mid = (low+high)//2
        left_low,left_high,left_sum = find_maximum_subarray(A,low,mid)
        right_low,right_high,right_sum = find_maximum_subarray(A,mid+1,high)
        cross_low,cross_high,cross_sum = find_max_crossing_subarray(A,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum :
            return left_low+1,left_high+1,left_sum
        else:
            if right_sum >= left_sum and right_sum >= cross_sum :
                return right_low+1,right_high+1,right_sum
            else:
                return cross_low,cross_high,cross_sum

def main():
    a=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,-15,-4,7]
    print(find_maximum_subarray(a,0,len(a)-1))

if __name__ == "__main__":
    main()