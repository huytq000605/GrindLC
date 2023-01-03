# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        def dfs(node):
            nonlocal arr
            
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        n = len(arr)
        s = set(arr)
        
        result = []
        for query in queries:
            if query in s:
                result.append([query, query])
                continue
            right = bisect_right(arr, query)
            left = right-1
            
            if left >= n or arr[left] > query:
                ans_left = -1
            else:
                ans_left = arr[left]
            
            if right >= n or arr[right] < query:
                ans_right = -1
            else:
                ans_right = arr[right]
            result.append([ans_left, ans_right])
        return result
