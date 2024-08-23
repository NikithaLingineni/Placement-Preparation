def fractionalknapsack(w,arr,n):
      arr.sort(key=lambda x:x.value/x.weight,reverse=True)
      curr=0
      p=0.0
      for i in range(n):
          if curr+arr[i].weight<=w:
              curr+=arr[i].weight
              p+=arr[i].value
          else:
              rem=w-curr
              p+=arr[i].value/arr[i].weight*rem
              break
      return p
