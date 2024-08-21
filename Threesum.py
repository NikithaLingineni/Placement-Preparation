def threesum(nums):
    n=len(nums)
    nums.sort()
    res=[]
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        j=i+1
        k=n-1
        while j<k:
            tot=nums[i]+nums[j]+nums[k]
            if tot<0:
                j+=1
            elif tot>0:
                k-=1
            else:
                res.append([nums[i],nums[j],nums[k]])
                j+=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
    return res
nums=list(map(int,input().split()))
result=threesum(nums)
print(result)
