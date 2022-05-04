from collections import deque

class MyStack:

    def __init__(self):
        self.queueIn = deque()
        self.queueOut = deque()


    def push(self, x: int) -> None:

        self.queueIn.append(x)


    def pop(self) -> int:

        if self.empty():
            return None
        
        for i in range(len(self.queueIn) - 1):
            self.queueOut.append(self.queueIn.popleft())

        self.queueIn, self.queueOut = self.queueOut,self.queueIn

        return self.queueOut.popleft()


    def top(self) -> int:

        if self.empty():
            return None

        res = self.queueIn[-1]

        return res



    def empty(self) -> bool:

        if self.queueIn :
            return False
        else:
            return True



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
# param_2 = obj.pop()
param_4 = obj.empty()

print(obj.top())

# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())