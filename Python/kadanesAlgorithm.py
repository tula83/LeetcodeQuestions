def largest_subarray_sum(arr):
    curr_sum,till=0,-9999
    for i in range(len(arr)):
        curr_sum+=arr[i]
        till=max(curr_sum,till)
        if(curr_sum<0):
            curr_sum=0
    return till


print(largest_subarray_sum([2,-1,3,2,-2]))
