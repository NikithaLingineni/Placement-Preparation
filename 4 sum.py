def foursum(nums,target):
    n=len(nums)
    res=[]
    nums.sort()
    for i in range(n-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            left=j+1
            right=n-1
            while left<right:
                tot=nums[i]+nums[j]+nums[left]+nums[right]
                if tot==target:
                    res.append([nums[i],nums[j],nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif tot<target:
                    left+=1
                else:
                    right-=1
    return res
nums=list(map(int,input().split()))
target=int(input())
res=foursum(nums,target)
print(res)                   
