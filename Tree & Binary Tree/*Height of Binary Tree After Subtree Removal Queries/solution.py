# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        levels = dict()
        cousins = defaultdict(list)
        def dfs(node, level):
            if not node:
                return 0
            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            depth = max(left, right) + 1
            levels[node.val] = level
            heappush(cousins[level], (depth, node.val))
            if len(cousins[level]) > 2:
                heappop(cousins[level])
            return depth
        
        dfs(root, 0)
        result = []
        
        for query in queries:
            level = levels[query]
            query_cousins = cousins[level]
            if len(query_cousins) == 1:
                result.append(level - 1)
            else:
                if query_cousins[1][1] != query:
                    result.append(level + query_cousins[1][0] - 1)
                else:
                    result.append(level + query_cousins[0][0] - 1)
        return result        
        
        
                
