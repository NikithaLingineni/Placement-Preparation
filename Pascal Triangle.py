def Pascal(n):
    triangle=[]
    for i in range(n):
        triangle.append(getrow(i))
    return triangle
def getrow(rowindex):
    ans=1
    res=[1]
    for i in range(rowindex):
        ans=ans*(rowindex-i)
        ans=ans/(i+1)
        res.append(int(ans))
    return res
n=int(input())
result=Pascal(n)
print(result)
