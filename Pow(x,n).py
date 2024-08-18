def power(x,n):
    p=n
    ans=1
    if p<0:
        p=-1*p
    while p>0:
        if p%2==1:
            ans=ans*x
            p-=1
        else:
            x=x*x
            p=p/2
    if n<0:
        ans=1/ans
    return ans
x=int(input())
n=int(input())
res=power(x,n)
print(res)
