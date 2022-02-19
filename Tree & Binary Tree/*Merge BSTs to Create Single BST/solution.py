# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
				
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        roots = {}
        count = Counter()
        for tree in trees:
            roots[tree.val] = tree
            left, right = tree.left, tree.right
            if left:
                count[left.val] += 1
            if right:
                count[right.val] += 1
            count[tree.val] += 1
        
        def dfs(node, min_value, max_value):
            if not node:
                return True
            if node.val <= min_value or node.val >= max_value:
                return False
            if node.left and node.left.val in roots:
                node.left = roots[node.left.val]
                roots.pop(node.left.val)
            if not dfs(node.left, min_value, node.val):
                return False
            if node.right and node.right.val in roots:
                node.right = roots[node.right.val]
                roots.pop(node.right.val)
            if not dfs(node.right, node.val, max_value):
                return False
            return True
        
        for tree in trees:
            if count[tree.val] == 1:
                if not dfs(tree, -math.inf, math.inf):
                    return None
                if len(roots) == 1:
                    return tree
                else:
                    return None
        return None