def maximumMeetings(n,start,end):
      meet=[(start[i],end[i],i+1) for i in range(n)]
      meet.sort(key=lambda x:(x[1],x[2]))
      ans=[]
      limit=meet[0][1]
      ans.append(meet[0][2])
      for i in range(1,n):
          if meet[i][0]>limit:
              limit=meet[i][1]
              ans.append(meet[i][2])
      return len(ans)
