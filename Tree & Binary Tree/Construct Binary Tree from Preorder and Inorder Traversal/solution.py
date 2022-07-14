# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(p_start, p_end, i_start, i_end):
            if p_start > p_end:
                return None
            root_value = preorder[p_start]
            inorder_root = i_start
            while inorder[inorder_root] != root_value:
                inorder_root += 1
            moves = inorder_root - i_start
            root_node = TreeNode(root_value)
            root_node.left = build(p_start + 1, p_start + moves, i_start, inorder_root - 1)
            root_node.right = build(p_start + moves + 1, p_end, inorder_root + 1, i_end)
            return root_node
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
