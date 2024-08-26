def common(l):
    a=max(l)
    b=min(l)
    n=min(len(a),len(b))
    c=""
    for i in range(n):
        if a[i]==b[i]:
            c+=a[i]
        else:
            break
    return c
l=list(map(str,input().split()))
res=common(l)
print(res)
