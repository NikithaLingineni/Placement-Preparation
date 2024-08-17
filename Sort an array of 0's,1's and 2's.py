def sorting(nums):
    n=len(nums)
    low=0
    mid=0
    high=n-1
    for i in range(n):
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        elif nums[mid]==2:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
nums=list(map(int,input().split()))
sorting(nums)
print(nums)
