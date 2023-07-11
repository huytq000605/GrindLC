# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = dict()
        def dfs(node, parent):
            if not node: return
            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        s = 0
        seen = set([target])
        dq = deque([target])
        while dq and s < k:
            for _ in range(len(dq)):
                node = dq.popleft()
                for next_node in [node.left, node.right, parents[node]]:
                    if next_node and next_node not in seen:
                        seen.add(next_node)
                        dq.append(next_node)
            s += 1
        return list([node.val for node in dq])
