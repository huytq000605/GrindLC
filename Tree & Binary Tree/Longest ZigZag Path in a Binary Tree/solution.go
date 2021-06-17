package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestZigZag(root *TreeNode) int {
	left := dfs(root, 0, true)
	right := dfs(root, 0, false)
	if left > right {
		return left - 1
	} else {
		return right - 1
	}
}

func dfs(node *TreeNode, current int, goLeft bool) int { // current is number of nodes
	if node == nil {
		return current
	}
	left := 0
	right := 0
	if goLeft {
		left = dfs(node.Left, 1+current, false) // go left and increase the node
		right = dfs(node.Left, 0, true)         // go left and reset, go to other direction ( if go to same direction, its result < the above result)
	} else {
		left = dfs(node.Right, 1+current, true)
		right = dfs(node.Right, 0, false)
	}
	if left > right {
		return left
	} else {
		return right
	}
}
