from collections import deque

class MyStack:

    def __init__(self):
        self.que = deque()


    def push(self, x: int) -> None:

        self.que.append(x)


    def pop(self) -> int:

        if self.empty():
            return None

        # return self.que.pop()

        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())

        return self.que.popleft()
        

    def top(self) -> int:

        if self.empty():
            return None

        res = self.que[-1]

        return res



    def empty(self) -> bool:

        if self.que :
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

# print(obj.top())

print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())