def knapsack(p,wt,c,n):
    dp=[[0 for j in range(c+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(c+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif wt[i-1]<=j:
                dp[i][j]=max(dp[i-1][j],p[-1]+dp[i-1][j-wt[i-1]])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][c]
p=list(map(int,input().split()))
wt=list(map(int,input().split()))
c=int(input())
n=len(p)
res=knapsack(p,wt,c,n)
print(res)
