def longest(nums):
    n=len(nums)
    if n==0:
        return 0
    longest=1
    s=set()
    for i in range(n):
        s.add(nums[i])
    for i in s:
        if i-1 not in s:
            cnt=1
            x=i
            while x+1 in s:
                x+=1
                cnt+=1
                longest=max(longest,cnt)
    return longest
nums=list(map(int,input().split()))
res=longest(nums)
print(res)
