def rotate(matrix):
    m=len(matrix)
    n=len(matrix[0])
    for i in range(m):
        for j in range(i,m):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(m):
        matrix[i].reverse()
    return matrix
r=int(input())
c=int(input())
matrix=[]
for i in range(r):
    ro=[]
    for j in range(c):
        ro.append(int(input()))
    matrix.append(ro)
res=rotate(matrix)
print(res)
