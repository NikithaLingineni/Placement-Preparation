def __init__(self):
    self.arr=[]
    self.rear=0
    self.front=0
def push(self,data):
    self.arr.append(data)
    self.rear+=1
def pop(self):
    if self.rear==self.front:
        return -1
    else:
        x=self.arr[self.front]
        self.front+=1
        return x
