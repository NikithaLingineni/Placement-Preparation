def maximum(nums):
    n=len(nums)
    c=0
    m=0
    for i in nums:
        if i==1:
            c+=1
            m=max(c,m)
        else:
            c=0
    return m

nums=list(map(int,input().split()))
result=maximum(nums)
print(result)
