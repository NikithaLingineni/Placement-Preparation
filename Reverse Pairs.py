def merge(arr,b, lb, mid, ub):
    i = lb
    j = mid + 1
    k = lb
    while i <= mid and j <= ub:
        if arr[i] <= arr[j]:
            b[k] = arr[i]
            i += 1
        else:
            b[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        b[k] = arr[i]
        i += 1
        k += 1

    while j <= ub:
        b[k] = arr[j]
        j += 1
        k += 1

    for k in range(lb, ub + 1):
        arr[k] = b[k]

def countPairs(arr, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt

def mergesort(arr,b,lb, ub):    
    cnt = 0
    if lb < ub:
        mid = (lb + ub) // 2
        cnt += mergesort(arr,b, lb, mid)
        cnt += mergesort(arr,b, mid + 1, ub)
        cnt += countPairs(arr, lb, mid, ub)
        merge(arr,b, lb, mid, ub)
    return cnt
def reversePairs(nums):
    n=len(nums)
    b = [0] * n
    return mergesort(nums,b, 0, n - 1)

nums=list(map(int,input().split()))
res=reversePairs(nums)
print(res)
