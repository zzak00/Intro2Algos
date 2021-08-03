# Maximum subarray problem

def find_max_crossing_subarray(A,low,mid,high):
    left_sum = -1*float('inf')
    sum = 0
    for i in range(mid,low+1,-1):
        sum+=A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -1*float('inf')
    sum = 0
    for j in range(mid+1,high+1):
        sum += A[j]
        if sum > right_sum :
            right_sum = sum
            max_right = j
    return max_left+1,max_right+1,left_sum+right_sum

def main():
    a=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,-15,-4,7]
    print(find_max_crossing_subarray(a,0,9,len(a)-1))

if __name__ == "__main__":
    main()