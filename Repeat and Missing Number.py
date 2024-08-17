def find(nums):
    n=len(nums)
    sn=n*(n+1)//2
    s2n=(n*(n+1)*(2*n+1))//6
    s=0
    s2=0
    for i in range(n):
        s+=nums[i]
        s2+=nums[i]*nums[i]
    val1=s-sn
    val2=s2-s2n
    val2=val2/val1
    x=(val1+val2)/2
    y=x-val1
    return [int(x),int(y)]
nums=list(map(int,input().split()))
res=find(nums)
print(res)
