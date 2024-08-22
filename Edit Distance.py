def edit(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0 for j in range(n+1)]for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 and j==0:
                dp[i][j]=0
            elif i==0 and j!=0:
                dp[i][j]=j
            elif i!=0 and j==0:
                dp[i][j]=i   
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    return dp[m][n]
s1=input()
s2=input()
res=edit(s1,s2)
print(res)
