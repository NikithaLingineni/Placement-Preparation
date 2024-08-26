def atoi(s):
    i,base,sign=0,0,1
    INT_MAX,INT_MIN=2147483647,-2147483648
    while i <len(s) and s[i]==' ':
        i+=1
    if i<len(s) and (s[i]=='-' or s[i]=='+'):
        sign=1-2*(s[i]=='-')
        i+=1
    while (i<len(s) and s[i]>='0' and s[i]<='9'):
        if (base>(INT_MAX//10) or (base==(INT_MAX//10) and (ord(s[i])-ord('0'))>7)):
            if sign==1:
                return INT_MAX
            else:
                return INT_MIN
        base=base*10+(ord(s[i])-ord('0'))
        i+=1
    return base*sign
s=input()
res=atoi(s)
print(res)    
