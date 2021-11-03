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
def sum_numbers(root)
    @result = 0
    def dfs(node, current)
        if node == nil 
            return
        end
        current = current * 10 + node.val
        if node.left == nil && node.right == nil 
            @result += current
            return
        end
        dfs(node.left, current)
        dfs(node.right, current)
    end
    dfs(root, 0)
    return @result
end