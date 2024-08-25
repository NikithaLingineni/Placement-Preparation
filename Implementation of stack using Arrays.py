def __init__(self):
  self.arr=[]
  self.top=-1
def push(self,data):
  self.top+=1
  if self.top<len(self.arr):
    self.arr[self.top]=data
  else:
    self.arr.append(data)
def pop(self):
  if self.top==-1:
    return -1
  else:
    x=self.arr[self.top]
    self.top-=1
    return x

