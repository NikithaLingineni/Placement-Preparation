def duplicate(nums):
    n=len(nums)
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    m=max(d.values())
    for key,value in d.items():
        if value==m:
            return key
nums=list(map(int,input().split()))
res=duplicate(nums)
print(res)
