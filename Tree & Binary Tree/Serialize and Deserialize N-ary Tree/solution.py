"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root: return ""
        result = f"{root.val}["
        for child in root.children:
            s = self.serialize(child)
            result += s
            result += ","
        if root.children: result = result[:-1] # remove last ","
        result += "]"
        return result
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: Node
        """
        if not data: return None
        val = ""
        i = 0
        for i in range(len(data)):
            if data[i] == "[":
                break
            val += data[i]
        children = []
        children_data = data[i+1:-1]
        stack = 0
        s = ""
        
        for c in children_data:
            if c == "[":
                stack += 1
            elif c == "]":
                stack -= 1
            elif c == ",":
                if not stack:
                    children.append(s)
                    s = ""
                    continue
            s += c
        if s:
            children.append(s)
        return Node(int(val), [self.deserialize(child) for child in children])
        

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
