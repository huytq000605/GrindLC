package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestZigZag(root *TreeNode) int {
	result := 0
	dfs(root, true, 1, &result)
	dfs(root, false, 1, &result)
	return result
}

func dfs(node *TreeNode, goLeft bool, height int, result *int) {
	if node == nil { // When node is nil, then we count the height of the tree
		if height-2 > *result { // -2 because last node is nil, number of left/right step is number of nodes - 1 => -2
			*result = height - 2
		}
		return
	}
	if goLeft {
		dfs(node.Left, false, height+1, result) // Go the left and + 1 height
		dfs(node.Left, true, 1, result)         // We make the left as starting point, but different direction from above because it will always get the lower result => we are finding max
	} else {
		dfs(node.Right, true, height+1, result)
		dfs(node.Right, false, 1, result)
	}
}
