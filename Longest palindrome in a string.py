def longest(s):
    n=len(s)
    dp=[[0]*n for i in range(n)]
    maxsize=1
    startindex=0
    for i in range(n):
        dp[i][i]=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=1
            maxsize=2
            startindex=i
    for length in range(3,n+1):
        for i in range(n-length+1):
            j=i+length-1
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j]=1
                if length>maxsize:
                    maxsize=length
                    startindex=i
    return s[startindex:startindex+maxsize]
s=input()
res=longest(s)
print(res)
