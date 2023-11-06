#knapsack problem 

def  max_values(wt,value,given_wt):
    n=len(value)
   
    dp=[[0 for j in range(given_wt+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(given_wt+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif wt[i-1]<=given_wt:
                dp[i][j]=max(value[i-1]+dp[i-1][j- wt[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][given_wt]

profit = [60, 100, 120] 
weight = [10, 20, 50] 
W = 50

print(f'maximum values {max_values(weight,profit,W)}')
