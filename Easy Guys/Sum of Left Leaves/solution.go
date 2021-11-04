package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) int {
	result := 0
	var dfs func(*TreeNode, bool)
	dfs = func(node *TreeNode, parentGoLeft bool) {
		if node == nil {
			return
		}
		if node.Left == nil && node.Right == nil && parentGoLeft {
			result += node.Val
		}
		dfs(node.Left, true)
		dfs(node.Right, false)
	}

	dfs(root, false)
	return result
}
