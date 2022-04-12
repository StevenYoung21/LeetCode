
class NodeList:
    def __init__(self, val):
        self.val = val
        self.next = None

# def create_linked_list(nums):
#     if len(nums) == 0:
#         return None
#     head = Node(nums[0])
#     cur = head
#     for i in range(1, len(nums)):
#         cur.next = Node(nums[i])
#         cur = cur.next
#     return head

# 打印链表
def print_linked_list(list_node):
    if list_node is None:
        return

    cur = list_node
    while cur:
        print(cur.val, '->', end=' ')
        cur = cur.next
    print('null')

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0 : return -1  ## 注意size等于号
        if index == 0 : return self.head.val

        cur = self.head
        pos = 1
        while cur.next:
            cur = cur.next    
            if pos == index:
                return cur.val
            pos +=1

    def addAtHead(self, val: int) -> None:
        curNode = NodeList(val)  ## 定义当前插入节点
        if self.size == 0:
            self.head = curNode
            self.size += 1
            return
        else:
            curNode.next = self.head
            self.head = curNode
            self.size += 1
            return

    def addAtTail(self, val: int) -> None:
        curNode = NodeList(val)
        if self.size == 0:
            self.head = curNode
            self.size += 1
        else:
           cur = self.head   ## 定义一个指针, 把头指针赋值给它, 这样可以移动cur指针寻找链表尾部
           while cur.next :
               cur = cur.next
           cur.next = curNode
           self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        curNode = NodeList(val)
        if index == 0 or index < 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > self.size :
            return -1
        else:
            cur = self.head
            pos = 1
            while cur.next :
                if pos == index :
                    curNode.next = cur.next 
                    cur.next = curNode
                pos +=1
                cur = cur.next    
            self.size += 1    
        return

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0 : return -1  ## 注意size等于号
        if index == 0 : 
            self.head = self.head.next
            self.size -= 1
            return
        if index == self.size - 1 :
            cur = self.head
            while cur.next.next != None:
                cur = cur.next
            cur.next = None
            self.size -= 1
            return 

        pos = 1
        cur = self.head
        while cur.next:
            if pos == index :
              cur.next = cur.next.next
            pos += 1
            cur = cur.next
        self.size -= 1
        return
        
        



# Your MyLinkedList object will be instantiated and called as such:




obj = MyLinkedList()


obj.addAtTail(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)

res1 = obj.get(1)
print(res1)

obj.deleteAtIndex(1)

res2 = obj.get(2)
print(res2)
# obj.addAtHead(3)
# obj.addAtHead(2)
# obj.addAtHead(5)
# obj.addAtTail(5)

# print(res1)
# res1 =  obj.get(4)

# print(res1)
# obj.deleteAtIndex(1)
print_linked_list(obj.head)


# param_1 = obj.get(2)

# print_linked_list(obj)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)