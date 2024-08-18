def majority(nums):
    n=len(nums)
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for key in d:
        if d[key]>n/2:
            return key
nums=list(map(int,input().split()))
res=majority(nums)
print(res)
