class MyQueue:

    def __init__(self):
        
        self.stackIn = []
        self.stackOut = []


    def push(self, x: int) -> None:
        self.stackIn.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stackOut:
            return self.stackOut.pop()
        else:
            for i in range(len(self.stackIn)):
                self.stackOut.append(self.stackIn.pop())
            
            return self.stackOut.pop()

    def peek(self) -> int:

        res = self.pop()
        self.stackOut.append(res)
        return res


    def empty(self) -> bool:
        if  self.stackIn or self.stackOut:
            return False
        else:
            return True



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

q1 = MyQueue()

q1.push(1)
q1.push(2)
q1.push(3)

print(q1.pop())
q1.push(4)

print(q1.peek())

