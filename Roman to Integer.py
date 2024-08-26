def roman(s):
    n=len(s)
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    num=d[s[n-1]]
    for i in range(n-2,-1,-1):
        if d[s[i]]>=d[s[i+1]]:
            num=num+d[s[i]]
        else:
            num=num-d[s[i]]
    return num
s=input()
res=roman(s)
print(res)
