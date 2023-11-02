def longest_pallindromic_subsequence(s):
    n=len(s)
    dp=[[0]*n for i in range(n)]
    print(dp)
    for i in range(n):
        dp[i][i]=1
    
    for c1 in range(2,n+1):
        for i in range(n-c1+1):
            j=i+c1-1

            if s[i]==s[j] and c1==2:
                dp[i][j]=2
            elif s[i]==s[j]:
                dp[i][j]=dp[i+1][j-1]+2
            else:
                dp[i][j]=max(dp[i][j-1],dp[i+1][j])
    return dp[0][n-1]

print('longest pallindromic subsequence ',longest_pallindromic_subsequence("bbbab"))