def JobScheduling(Jobs,n):
      Jobs.sort(key=lambda x:x.profit,reverse=True)
      m=Jobs[0].deadline
      for i in range(n):
          m=max(m,Jobs[i].deadline)
      slot=[-1]*(m+1)
      cnt=0
      p=0
      for i in range(n):
          for j in range(Jobs[i].deadline,0,-1):
              if slot[j]==-1:
                  slot[j]=i
                  cnt+=1
                  p+=Jobs[i].profit
                  break
      return cnt,p
