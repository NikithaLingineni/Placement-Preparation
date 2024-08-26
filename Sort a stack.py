def sortinsert(s,element):
    if len(s)==0 or element>s[-1]:
        s.append(element)
        return
    else:
        temp=s.pop()
        sortinsert(s,element)
        s.append(temp)
def sort(s):
    if len(s)!=0:
        temp=s.pop()
        sort(s)
        sortinsert(s,temp)
s=list(map(int,input().split()))
res=sort(s)
print(s)
