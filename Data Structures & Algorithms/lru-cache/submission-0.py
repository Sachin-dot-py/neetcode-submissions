class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __remove(self, key: int) -> int:
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[key]
        return node.value

    def __insert(self, key: int, value: int):
        node = Node(key, value)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

        self.cache[key] = node

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.__remove(key)
        else:
            return -1
        self.__insert(key, value)
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.__remove(key)
            self.capacity += 1
        self.__insert(key, value)
        if self.capacity == 0:
            key = self.head.next.key
            self.__remove(key)
        else:
            self.capacity -= 1
