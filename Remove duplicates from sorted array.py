def duplicates(nums):
    n=len(nums)
    if n==1:
        return 1
    else:
        j=0
        count=1
        for i in range(1,n):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
                count+=1
        return count

nums=list(map(int,input().split()))
result=duplicates(nums)
print(result)
