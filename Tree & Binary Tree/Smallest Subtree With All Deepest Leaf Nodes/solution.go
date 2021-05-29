/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
    result, _ := helper(root, 0)
    return result
}

func helper(current *TreeNode, level int) (*TreeNode, int) {
    if current.Left == nil && current.Right == nil {
        return current, level
    }
    if current.Left == nil {
        return helper(current.Right, level + 1)
    }
    if current.Right == nil {
        return helper(current.Left, level + 1)
    }
    
    left, levelLeft := helper(current.Left, level + 1)
    right, levelRight := helper(current.Right, level + 1)
    
        if levelLeft > levelRight {
            return left, levelLeft
        }
        if levelLeft < levelRight {
            return right,levelRight
        }
        return current, levelLeft
    
}