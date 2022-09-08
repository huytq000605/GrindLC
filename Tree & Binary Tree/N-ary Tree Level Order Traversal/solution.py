"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            result.append([])
            nq = deque()
            while q:
                node = q.popleft()
                result[-1].append(node.val)
                for child in node.children:
                    nq.append(child)
            q, nq = nq, q
        return result
