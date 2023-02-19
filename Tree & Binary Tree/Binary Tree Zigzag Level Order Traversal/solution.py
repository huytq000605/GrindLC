# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ltr = True
        dq = deque([root])
        result = []
        while dq:
            result.append([])
            ndq = deque()
            while dq:
                node = dq.popleft()
                result[-1].append(node.val)
                if node.left:
                    ndq.append(node.left)
                if node.right:
                    ndq.append(node.right)
            if not ltr:
                result[-1] = result[-1][::-1]
            ltr = not ltr
            dq = ndq
        return result
                    
            

