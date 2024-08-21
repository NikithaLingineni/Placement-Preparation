def trapping(heights):
    n=len(heights)
    left=0
    right=n-1
    leftmax,rightmax,res=0,0,0
    while left<=right:
        if heights[left]<=heights[right]:
            if heights[left]>leftmax:
                leftmax=heights[left]
            else:
                res+=leftmax-heights[left]
            left+=1
        else:
            if heights[right]>rightmax:
                rightmax=heights[right]
            else:
                res+=rightmax-heights[right]
            right-=1
    return res

heights=list(map(int,input().split()))
result=trapping(heights)
print(result)
