def search(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    start=0
    end=n*m-1
    while start<=end:
        mid=(start+end)//2
        i=mid//m
        j=mid%m
        if target==matrix[i][j]:
            return True
        elif target<matrix[i][j]:
            end=mid-1
        else:
            start=mid+1
    return False

r=int(input())
c=int(input())
matrix=[]
for i in range(r):
    ro=[]
    for j in range(c):
        ro.append(int(input()))
    matrix.append(ro)
target=int(input())
res=search(matrix,target)
print(res)
