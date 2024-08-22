def longestsum(nums):
    n=len(nums)
    dp=[nums[i] for i in range(n)]
    for i in range(n):
        for j in range(0,i):
            if nums[i]>nums[j] and dp[i]<dp[j]+nums[i]:
                dp[i]=dp[j]+nums[i]
    m=max(dp)
    return m
nums=list(map(int,input().split()))
res=longestsum(nums)
print(res)
