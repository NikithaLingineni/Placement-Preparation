def setmatrix(matrix):
    m=len(matrix)
    n=len(matrix[0])
    row=set()
    col=set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                row.add(i)
                col.add(j)
    for i in row:
        for j in range(n):
            matrix[i][j]=0
    for j in col:
        for i in range(m):
            matrix[i][j]=0
    return matrix
r=int(input())
c=int(input())
matrix=[]
for i in range(r):
    ro=[]
    for j in range(c):
        ro.append(int(input()))
    matrix.append(ro)
res=setmatrix(matrix)
print(res)
