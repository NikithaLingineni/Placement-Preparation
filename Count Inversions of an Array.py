def merge(arr,b,lb,mid,ub):
    i=lb
    j=mid+1
    k=ub
    cnt=0
    while i<=mid and j<=ub:
        if arr[i]<=arr[j]:
            b[k]=arr[i]
            i+=1
        else:
            b[k]=arr[j]
            cnt+=(mid-i+1)
            j+=1
        k+=1
    while i<=mid:
        b[k]=arr[i]
        i+=1
        k+=1
    while j<=ub:
        b[k]=arr[j]
        j+=1
        k+=1
    for k in range(lb,ub+1):
        arr[k]=b[k]
    return cnt

def  mergesort(arr,b,lb,ub):
    cnt=0
    if lb<ub:
        mid=(lb+ub)//2
        cnt+=mergesort(arr,b,lb,mid)
        cnt+=mergesort(arr,b,mid+1,ub)
        cnt+=merge(arr,b,lb,mid,ub)
    return cnt
def countinversions(arr):
    n=len(arr)
    b=[0]*n
    return mergesort(arr,b,0,n-1)

arr=list(map(int,input().split()))
res=countinversions(arr)
print(res)
