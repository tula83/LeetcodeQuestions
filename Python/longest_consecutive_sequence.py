#finding longest consecutive sequence in array

# Example 1:

# Input: [100, 200, 1, 3, 2, 4]

# Output: 4

# Explanation: The longest consecutive subsequence is 1, 2, 3, and 4

def longest_sequence(arr):
    n=len(arr)
    dp=[[0 for i in range(n+1)]for j in range(n+1)]


def longest_consecutive_subsequence(arr):
    if not arr:
        return 0

    num_set = set(arr)
    max_length = 1

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

# Example usage
arr = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_subsequence(arr)
print("Length of the longest consecutive subsequence is:", result)



#

def longest_consecutive_subsequence(arr):
    if not arr:
        return 0
    
    arr.sort()
    max_length = 1
    current_length = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_length += 1
        elif arr[i] != arr[i - 1]:
            current_length = 1
        max_length = max(max_length, current_length)

    return max_length

# Example usage
arr = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_subsequence(arr)
print("Length of the longest consecutive subsequence is:", result)

