def distinct_sum(nums):
    n=len(nums)
    subset_sums=set(nums)

    dp=[0] * (sum(nums)+1)
    dp[0]=1


    for num in nums:
        for i in range(len(dp)-1,-1,-1):
            if dp[i]:
                print(dp[i])
                
                dp[i+num]=1

    for i in range(len(dp)):
        if dp[i]:
            subset_sums.add(i)


    return list(subset_sums)

print(distinct_sum([1,2,3]))



# minimum squares

def MinSquares(self, n):
    dp = [float('inf')] * (n+1)
    dp[0] = 0

    for i in range(n+1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], 1 + dp[i-j*j])
            j += 1
            
    return dp[n]

		
# count subset  sum equal to target


def count_subsets_with_sum(nums, target_sum):
    n = len(nums)

    # Create a 2D table to store results of subproblems
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(n + 1)]

    # If the target sum is 0, then an empty subset always exists
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill the table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If the current element is greater than the target sum, exclude it
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Include the current element or exclude it
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]

    return dp[n][target_sum]

# Example usage
numbers = [3 ,34 ,4 ,12 ,5,2]
target = 9

result = count_subsets_with_sum(numbers, target)
print(f"The number of subsets with sum {target} is: {result}")
