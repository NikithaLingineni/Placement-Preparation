class MyStack:
    def __init(self):
        self.q=deque()
    def push(self,x):
        n=len(self.q)
        self.q.append(x)
        for i in range(n):
            self.q.append(self.q.popleft())
    def pop(self):
        p=self.q.popleft()
        return p
    def peek(self):
        return self.q[0]
    def isempty(self):
        return len(self.q)==0
