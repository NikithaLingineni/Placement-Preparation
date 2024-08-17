def maximum(nums):
    n=len(nums)
    max_start=nums[0]
    max_end=0
    for i in range(n):
        max_end+=nums[i]
        max_start=max(max_start,max_end)
        if max_end<0:
            max_end=0
    return max_start
nums=list(map(int,input().split()))
res=maximum(nums)
print(res)
