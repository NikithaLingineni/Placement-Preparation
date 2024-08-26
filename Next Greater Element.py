def nextgreater1(nums1,nums2):
    n=len(nums2)
    nge=[-1]*n
    st=[]
    d={}
    for i in range(n-1,-1,-1):
        while st and st[-1]<=nums2[i]:
            st.pop()
        if st:
            d[nums2[i]]=st[-1]
        else:
            d[nums2[i]]=-1
        st.append(nums2[i])
    ans=[]
    for i in nums1:
        ans.append(d[i])
    return ans
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
res=nextgreater1(nums1,nums2)
print(res)
