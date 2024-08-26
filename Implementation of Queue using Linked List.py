class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class MyQueue:
    def __init__(self):
        self.rear=None
        self.front=None
        self.size=0
    def push(self,item):
        temp=Node(item)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.size+=1
    def pop():
        if self.front==None:
            return -1
        else:
            x=self.front.data
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            self.size-=1
            return x
