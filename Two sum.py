def twosum(nums,target):
    n=len(nums)
    d={}
    for i in range(n):
        temp=target-nums[i]
        if temp in d:
            return [d[temp],i]
        d[nums[i]]=i
        
nums=list(map(int,input().split()))
target=int(input())
res=twosum(nums,target)
print(res)
