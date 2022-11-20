# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        result = 0
        while q:
            nq = deque()
            arr = []
            while q:
                node = q.popleft()
                if node.left:
                    nq.append(node.left)
                    arr.append(node.left.val)
                if node.right:
                    nq.append(node.right)
                    arr.append(node.right.val)
            sorted_arr = sorted(arr)
            correct_idx = dict()
            for i, num in enumerate(sorted_arr):
                correct_idx[num] = i
            for i, num in enumerate(arr):
                while correct_idx[num] != i:
                    arr[i], arr[correct_idx[num]] = arr[correct_idx[num]], arr[i]
                    num = arr[i]
                    result += 1
            q = nq
        return result
