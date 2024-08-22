def longest(nums):
    n=len(nums)
    l=[1]*n
    dp=[[nums[i]] for i in range(n)]
    for i in range(n):
        for j in range(0,i):
            if nums[i]>nums[j] and l[i]<l[j]+1:
                l[i]=l[j]+1
                dp[i]=dp[j]+[nums[i]]
    m=max(l)
    return m
nums=list(map(int,input().split()))
res=longest(nums)
print(res)
