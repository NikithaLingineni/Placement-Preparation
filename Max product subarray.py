def maxProduct(nums):
    n=len(nums)
    if n==1:
        return nums[0]
    prefix=1
    suffix=1
    maxi=0
    for i in range(n):
        if prefix==0:
            prefix=1
        if suffix==0:
            suffix=1
        prefix=prefix*nums[i]
        suffix=suffix*nums[n-i-1]
        maxi=max(maxi,max(prefix,suffix))
    return maxi
nums=list(map(int,input().split()))
res=maxProduct(nums)
print(res)
