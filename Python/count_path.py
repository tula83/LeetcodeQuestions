def  count_paths(n,m):
    dp=[[0 for i in range(m)]for j in range(n)]

    for i in range(m):
        dp[0][i]=1
    for j in range(n):
        dp[j][0]=1
    

    for  i in range(1,n):
        for j  in range(1,m):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]


    return dp[n-1][m-1]


print(f'unique paths are {count_paths(2,2)}')