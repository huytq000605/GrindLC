class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = dict()
        self.len = 0
    
    def delete(self, node):
        del self.d[node.k]
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.d:  return -1
        value = self.d[key].v
        self.put(key, value)
        
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            if self.len == self.cap:
                self.delete(self.head.next)
                self.len -= 1
        else:
            node = self.d[key]
            self.delete(node)
            self.len -= 1

        node = Node(key, value)
        self.d[key] = node
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.len += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
