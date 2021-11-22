# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = ""
        def dfs(node):
            nonlocal result
            if node == None:
                result += "#,"
                return
            result += f"{node.val},"
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result[:-1]
            
        

    def deserialize(self, data):
        arr = data.split(",")
        idx = 0
        def dfs():
            nonlocal idx, arr
            if arr[idx] == "#":
                idx += 1
                return None
            root = TreeNode(int(arr[idx]))
            idx += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
            
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))