#maximum  subarray with sum positive only

def ksum(arr):
    curr_sum,till=0,-9999

    for item in arr:
        if item >0:
            curr_sum+=item
            till=max(curr_sum,till)
        else:
            curr_sum=0
    return till

#print(ksum([1,2,3,1,2,9,-1,11,2]))

#longest  subarray with given sum k 

def longest_subarray(arr,k):
    n=len(arr)
    curr_sum=0
    length=1
    for i in range(len(arr)):
        for  j in range(i,n):
            if curr_sum<k:
                curr_sum+=arr[j]
                if curr_sum==k:
                    length=max(length,j-i+1)
            else:
                break
    return length

print(f'longest subarray length {longest_subarray([1, -1, 5, 2, 3],7)}')




#another method

def longest_subarray_with_sum(arr, k):
    max_length = 0
    sum_map = {}  # Dictionary to store cumulative sum and its index
    current_sum = 0

    for i, num in enumerate(arr):
        current_sum += num

        if current_sum == k:
            max_length = i + 1

        if current_sum - k in sum_map:
            max_length = max(max_length, i - sum_map[current_sum - k])

        if current_sum not in sum_map:
            sum_map[current_sum] = i

    return max_length

# Example usage
arr = [1, -1, 5, 2, 3]
k = 7
result = longest_subarray_with_sum(arr, k)
print("Length of the longest subarray with sum", k, "is:", result)
