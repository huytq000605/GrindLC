# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}
def sum_of_left_leaves(root)
    @result = 0
    
    def dfs(node, parentGoLeft)
        if node == nil
            return
        end
        
        if node.left == nil && node.right == nil && parentGoLeft
            @result += node.val
        end
        dfs(node.left, true)
        dfs(node.right, false)
    end
    
    dfs(root, false)
    return @result
end