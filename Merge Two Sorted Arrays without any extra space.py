def merge(nums1,nums2):
    n=len(nums1)
    m=len(nums2)
    l=n-1
    r=0
    while l>=0 and r<=m:
        if nums1[l]>nums2[r]:
            nums1[l],nums2[r]=nums2[r],nums1[l]
            l-=1
            r+=1
        else:
            break
    nums1.sort()
    nums2.sort()
nums1=list(map(int,input().split())) 
nums2=list(map(int,input().split()))
merge(nums1,nums2)
print(nums1,nums2)
