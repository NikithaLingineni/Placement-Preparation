def stock(nums):
    n=len(nums)
    min_profit=nums[0]
    max_profit=0
    for i in nums:
        if i<min_profit:
            min_profit=i
        else:
            max_profit=max(max_profit,i-min_profit)
    return max_profit
nums=list(map(int,input().split()))
res=stock(nums)
print(res)
