class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: Node
        self.head = Node(None, None) # dummy head node
        self.tail = Node(None, None) # dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def updateLRU(self, key):
        node = self.cache[key]
        # remove from LL
        node.prev.next = node.next
        node.next.prev = node.prev

        # add to end of LL
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.updateLRU(key)
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.updateLRU(key)
            self.cache[key].value = value
        else:
            node = Node(key, value)
            self.cache[key] = node

            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

            self.capacity -= 1

            if self.capacity < 0:
                removedNode = self.head.next
                del self.cache[removedNode.key]
                self.head.next = removedNode.next
                self.head.next.prev = self.head
                del removedNode
                self.capacity += 1
