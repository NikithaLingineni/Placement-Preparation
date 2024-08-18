def longestsubstring(s):
    n=len(s)
    d={}
    left=0
    maxi=0
    for right in range(n):
        if s[right] in d and d[s[right]]>=left:
            left=d[s[right]]+1
        d[s[right]]=right
        maxi=max(maxi,right-left+1)
    return maxi
s=input()
res=longestsubstring(s)
print(res)
