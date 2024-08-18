from collections import defaultdict
def count1(nums,k):
    n=len(nums)
    d=defaultdict(int)
    xr=0
    cnt=0
    d[xr]=1
    for i in range(n):
        xr=xr^nums[i]
        x=xr^k
        cnt+=d[x]
        d[xr]+=1
    return cnt
nums=list(map(int,input().split()))
k=int(input())
res=count1(nums,k)
print(res)
