# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mapping = dict()
        parent = dict()
        for p, c, l in descriptions:
            if p not in mapping:
                mapping[p] = TreeNode(p)
            if c not in mapping:
                mapping[c] = TreeNode(c)
            p, c = mapping[p], mapping[c]
            if l:
                p.left = c
            else:
                p.right = c
            parent[c] = p
        
        def dfs(child):
            if child not in parent:
                return child
            else:
                return dfs(parent[child])

        return dfs(mapping[descriptions[0][0]])