class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr != self.tail:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        self.size += 1

        new_node = Node(val)
        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next = new_node
        new_node.next.prev = new_node

    def addAtTail(self, val: int) -> None:
        self.size += 1
        
        new_node = Node(val)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        
        self.tail.prev = new_node
        new_node.prev.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            # don't insert
            return
        else:
            curr = self.head.next
            i = 0
            while curr != self.tail:
                if i == index:
                    # add at this position
                    new_node = Node(val)
                    new_node.prev = curr.prev
                    new_node.next = curr
                    
                    curr.prev.next = new_node
                    curr.prev = new_node

                    self.size += 1
                    break
                i += 1
                curr = curr.next
        

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size:
            # invalid
            return
        curr = self.head.next
        i = 0
        while curr != self.tail:
            if i == index:
                # remove at this position
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                del curr
                self.size -= 1
                break
            i += 1
            curr = curr.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)