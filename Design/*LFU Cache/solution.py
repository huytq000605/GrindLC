class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0

    def pop(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        self.len -= 1
    
    def append(self, key, val):
        prev_tail, tail = self.tail.prev, self.tail
        node = Node(key, val)
        prev_tail.next = node
        tail.prev = node
        node.next = tail
        node.prev = prev_tail
        self.len += 1
        return node
    
    def __len__(self):
        return self.len
    

class LFUCache:
    def __init__(self, capacity: int):
        self.key_to_count = dict()
        self.key_to_node = dict()
        self.count_to_dlist = defaultdict(DLL)
        self.min_count = 0
        self.cap = capacity
        
    def get(self, key: int) -> int:
        if key not in self.key_to_count:
            return -1
        count = self.key_to_count[key]
        dlist = self.count_to_dlist[count]
        node = self.key_to_node[key]
        dlist.pop(node)
        if len(dlist) == 0 and count == self.min_count:
            self.min_count = count + 1
        dlist = self.count_to_dlist[count + 1]
        node = dlist.append(key, node.val)
        self.key_to_count[key] = count + 1
        self.key_to_node[key] = node
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.key_to_count:
            self.get(key)
            self.key_to_node[key].val = value
        else:
            if len(self.key_to_count) == self.cap:
                dlist = self.count_to_dlist[self.min_count]
                node = dlist.head.next
                self.key_to_node.pop(node.key)
                self.key_to_count.pop(node.key)
                dlist.pop(node)

            self.min_count = 1
            node = self.count_to_dlist[1].append(key, value)
            self.key_to_node[key] = node
            self.key_to_count[key] = 1
        
                


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)