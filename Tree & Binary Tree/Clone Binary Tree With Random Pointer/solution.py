# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root: return None
        q = deque([root])
        mapping = dict()
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                v = NodeCopy(u.val, None, None, None)
                mapping[u] = v
                if u.left: q.append(u.left)
                if u.right: q.append(u.right)
        
        q = deque([root])
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                v = mapping[u]
                if u.random:
                    v.random = mapping[u.random]
                if u.left: 
                    v.left = mapping[u.left]
                    q.append(u.left)
                if u.right:
                    v.right = mapping[u.right]
                    q.append(u.right)
        return mapping[root]
