/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findTarget(root *TreeNode, k int) bool {
    stackLeft := make([]*TreeNode, 0)
    stackRight := make([]*TreeNode, 0)
    pushLeft := func(node *TreeNode) {
        for node != nil {
            stackLeft = append(stackLeft, node)
            node = node.Left
        }
    }
    
    pushRight := func(node *TreeNode) {
        for node != nil {
            stackRight = append(stackRight, node)
            node = node.Right
        }
    }
    
    nextLeft := func() *TreeNode {
        n := len(stackLeft)
        res := stackLeft[n-1]
        stackLeft = stackLeft[:n-1]
        pushLeft(res.Right)
        return res
    }
    
    nextRight := func() *TreeNode {
        n := len(stackRight)
        res := stackRight[n-1]
        stackRight = stackRight[:n-1]
        pushRight(res.Left)
        return res
    }
    
    pushLeft(root)
    pushRight(root)
    left, right := nextLeft(), nextRight()
    for left.Val < right.Val {
        s := left.Val + right.Val
        if s == k {
            return true
        } else if s < k {
            left = nextLeft()
        } else {
            right = nextRight()
        }
    }
    return false
}
