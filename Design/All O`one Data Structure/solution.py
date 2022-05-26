class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val
        self.keys = set()
    
    def pop(self):
        prev, nxt = self.prev, self.next
        prev.next = nxt
        nxt.prev = prev
class AllOne:
    def __init__(self):
        self.key_to_count = dict()
        self.count_to_node = dict()
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
         

    def inc(self, key: str) -> None: 
        if key not in self.key_to_count:
            count = 0
        else:
            count = self.key_to_count[key]
        self.key_to_count[key] = count + 1
        node = self.count_to_node.get(count, None) or self.head
        if node.next.val != count + 1:
            new_node = Node(count + 1)
            node.next.prev = new_node
            new_node.next = node.next
            new_node.prev = node
            node.next = new_node
            self.count_to_node[count + 1] = new_node
        node.next.keys.add(key)
        node.keys.discard(key)
        
        # Remove this node if there isn't any keys in it
        if node.val != 0 and len(node.keys) == 0:
            self.count_to_node.pop(count)
            node.pop()
            
            
    def dec(self, key: str) -> None:
        if key in self.key_to_count:
            count = self.key_to_count[key]
            self.key_to_count[key] = count - 1
            node = self.count_to_node[count]
            node.keys.discard(key)
            
            # if count == 1 then we just remove the key
            if count == 1:
                self.key_to_count.pop(key)
            else:
            # move the key to the prev node in doubly linkedlist
                if node.prev.val != count - 1:
                    prev_node = Node(count - 1)
                    prev_node.prev = node.prev
                    prev_node.next = node
                    node.prev.next = prev_node

                    node.prev = prev_node
                    self.count_to_node[count - 1] = prev_node
                node.prev.keys.add(key)
            
            # Remove this node if there isn't any keys in it
            if len(node.keys) == 0:
                self.count_to_node.pop(count)
                node.pop()
            
    def getMaxKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        result = self.tail.prev.keys.pop()
        self.tail.prev.keys.add(result)
        return result

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        result = self.head.next.keys.pop()
        self.head.next.keys.add(result)
        return result


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()