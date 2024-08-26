def reversewords(s):
    s=s.strip()
    n=len(s)
    left=0
    right=n-1
    temp=""
    ans=""
    while left<=right:
        ch=s[left]
        if ch!=' ':
            temp+=ch
        elif ch==' ' and temp:
            if ans!="":
                ans=temp+" "+ans
            else:
                ans=temp
            temp=""
        left+=1
    if temp!="":
        if ans!="":
            ans=temp+" "+ans
        else:
            ans=temp
    return ans
s=input()
res=reversewords(s)
print(res)
