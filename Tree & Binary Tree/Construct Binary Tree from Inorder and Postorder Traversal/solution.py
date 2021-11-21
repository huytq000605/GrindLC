# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(sI, eI, sP, eP):
            if sI > eI:
                return None
            root = TreeNode(postorder[eP])
            rootIdx = sI
            for i in range(sI, eI + 1):
                if inorder[i] == postorder[eP]:
                    rootIdx = i
                    break
            numOfLeftNodes = rootIdx - 1 - sI + 1
            root.left = build(sI, rootIdx - 1, sP, sP + numOfLeftNodes - 1)
            root.right = build(rootIdx + 1, eI, sP + numOfLeftNodes, eP - 1)
            return root
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)