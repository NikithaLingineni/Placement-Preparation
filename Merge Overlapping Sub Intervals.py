def merge(intervals):
    intervals=sorted(intervals,key=lambda x:x[0])
    ans=[]
    for interval in intervals:
        if not ans or ans[-1][1]<interval[0]:
            ans.append(interval)
        else:
            ans[-1][1]=max(ans[-1][1],interval[1])
    return ans
r=int(input())
c=int(input())
intervals=[]
for i in range(r):
    ro=[]
    for j in range(c):
        ro.append(int(input()))
    intervals.append(ro)
res=merge(intervals)
print(res)
