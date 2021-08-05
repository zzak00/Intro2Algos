# Maximum subarray problem

def find_max_crossing_subarray(A,low,mid,high):
    left_sum = -1*float('inf')
    max_left=mid
    sum = 0
    for i in range(mid,low-1,-1):
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
    return max_left,max_right,left_sum+right_sum


def find_maximum_subarray(A,low,high):
    if high == low :
        return (low,high,A[low])
    else :
        mid = (low+high)//2
        left_low,left_high,left_sum = find_maximum_subarray(A,low,mid)
        right_low,right_high,right_sum = find_maximum_subarray(A,mid+1,high)
        cross_low,cross_high,cross_sum = find_max_crossing_subarray(A,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum :
            return left_low,left_high,left_sum
        else:
            if right_sum >= left_sum and right_sum >= cross_sum :
                return right_low,right_high,right_sum
            else:
                return cross_low,cross_high,cross_sum


def max_suba_l(a):
    l = r = 0
    max_sum = a[0]
    sum_now = a[0]
    for j in range(0,len(a)-2):
        print(sum_now)
        sum_now+=a[j+1]
        if sum_now >= max_sum :
                r= j+1
                max_sum=sum_now
        else :
            if a[j] + a[j+1] >= max_sum :
                l=j
                r=j+1
                max_sum=a[j]+a[j+1]
                sum_now=a[j]+a[j+1]
    return (l,r,max_sum)

from sys import maxsize
 
# Function to find the maximum contiguous subarray
# and print its starting and end index
def maxSubArraySum(a,size):
 
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0,size):
 
        max_ending_here += a[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
 
    print ("Maximum contiguous sum is %d"%(max_so_far))
    print ("Starting Index %d"%(start))
    print ("Ending Index %d"%(end))
 
# Driver program to test maxSubArraySum

def main():
    a=[13,3,-25,-20,8,16,-23,18,20,-7,-12,-5,-22,-15,-4,7]
    #print(max_suba_l(a))
    maxSubArraySum(a,len(a))
if __name__ == "__main__":
    main()