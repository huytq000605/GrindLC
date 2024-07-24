# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        stack = [root]
        ups = dict()
        start, dest = None, None

        def find_lca(u, p):
            nonlocal start, dest
            if not u: return None
            if p: ups[u] = p
            if u.val == startValue: start = u
            if u.val == destValue: dest = u
            left = find_lca(u.left, u)
            right = find_lca(u.right, u)
            if u == start or u == dest:
                return u 
            if left and right:
                return u
            if left or right:
                return left or right
            return None

        lca = find_lca(root, None)

        start_to_lca = ""
        while start != lca:
            start_to_lca += "U"
            start = ups[start]
        
        dest_to_lca = ""
        while dest != lca:
            ndest = ups[dest]
            if ndest.left == dest:
                dest_to_lca += "L"
            else:
                dest_to_lca += "R"
            dest = ndest
        return start_to_lca + dest_to_lca[::-1]
