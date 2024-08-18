import math
def majority1(nums):
    n=len(nums)
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    x=math.floor(n/3)
    l=[]
    for key in d:
        if d[key]>x:
            l.append(key)
    return l
nums=list(map(int,input().split()))
res=majority1(nums)
print(res)
