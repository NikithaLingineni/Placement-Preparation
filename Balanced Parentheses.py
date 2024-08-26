def isValid(s):
    l=[]
    for i in range(len(s)):
        if (s[i]=='{' or s[i]=='[' or s[i]=='('):
            l.append(s[i])
        else:
            if not l:
                return False
            if ((s[i]=='}' and l[-1]=='{') or (s[i]==']' and l[-1]=='[') or (s[i]==')' and l[-1]=='(')):
                l.pop()
            else:
                return False
    return len(l)==0
