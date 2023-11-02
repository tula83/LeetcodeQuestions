#minimum number of coins to make  denominations

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)

        dp=[[0 for j in  range(amount+1)] for i in range(len(coins)+1)]

        for i in range(len(coins)+1):
            for j in range(amount+1):
                if  i==0:
                    dp[i][j]=1e5+1
                elif j==0:
                    dp[i][j]=0
                elif j>=coins[i-1]:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
        if dp[n][amount]==1e5+1:
            return -1
        else:
            return dp[n][amount]

        
        