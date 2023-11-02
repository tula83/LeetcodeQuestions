#longest subarray with sum  k positive

def ksum(arr):
    curr_sum,till=0,-9999

    for item in arr:
        if item >0:
            curr_sum+=item
            till=max(curr_sum,till)
        else:
            curr_sum=0
    return till

print(ksum([1,2,3,1,2,9,-1,11,2]))
