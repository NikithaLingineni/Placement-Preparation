def minimumPlatform(n,arr,dep):
      arr.sort()
      dep.sort()
      i=0
      j=0
      cnt=0
      maxcnt=0
      while i<n:
          if arr[i]<=dep[j]:
              cnt+=1
              i+=1
          else:
              cnt-=1
              j+=1
          maxcnt=max(maxcnt,cnt)
      return maxcnt
