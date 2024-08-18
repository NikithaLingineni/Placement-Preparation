def largest(nums):
    n=len(nums)
    sum1=0
    maxi=0
    d={}
    for i in range(n):
        sum1+=nums[i]
        if sum1==0:
            maxi=i+1
        else:
            if sum1 in d:
                maxi=max(maxi,i-d[sum1])
            else:
                d[sum1]=i
    return maxi
nums=list(map(int,input().split()))
res=largest(nums)
print(res)
