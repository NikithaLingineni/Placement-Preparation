# class StackNode
def __init__(self):
    self.stack=None
def push(self,data):
    newnode=StackNode(data)
    newnode.next=self.stack
    self.stack=newnode
def pop(self):
    if self.stack:
        x=self.stack.data
        self.stack=self.stack.next
        return x
    return -1
