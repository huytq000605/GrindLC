
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        result = []
        xs = defaultdict(list)
        dq = deque([(root, 0)])
        mn, mx = math.inf, -math.inf
        while dq:
            node, x = dq.popleft()
            mn = min(mn, x)
            mx = max(mx, x)
            xs[x].append(node.val)
            if node.left: dq.append((node.left, x-1))
            if node.right: dq.append((node.right, x+1))
        for x in range(mn, mx+1):
            result.append(xs[x])
        return result

