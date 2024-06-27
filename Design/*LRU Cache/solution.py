class Node:
    def __init__(self, key, prev, next):
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = Node(0, None, None)
        self.tail = Node(0, self.head, None)
        self.head.next = self.tail
        self.node_map = dict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.move_to_head(self.node_map[key])
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.move_to_head(self.node_map[key])
        else:
            if len(self.cache) == self.cap:
                evict_node = self.tail.prev
                evict_key = evict_node.key
                del self.cache[evict_key]
                del self.node_map[evict_key]
                evict_node.prev.next = self.tail
                self.tail.prev = evict_node.prev
                del evict_node
            
            self.cache[key] = value
            self.node_map[key] = Node(key, self.head, self.head.next)
            self.head.next.prev = self.node_map[key]
            self.head.next = self.node_map[key]
            

    def move_to_head(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
