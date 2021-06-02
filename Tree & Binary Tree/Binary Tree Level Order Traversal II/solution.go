package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrderBottom(root *TreeNode) [][]int {
	height := getHeight(root)
	result := make([][]int, height)
	helper(root, 0, &result)
	return result
}

func helper(node *TreeNode, level int, result *[][]int) {
	if node == nil {
		return
	}
	helper(node.Left, level+1, result)
	helper(node.Right, level+1, result)
	(*result)[len(*result)-1-level] = append((*result)[len(*result)-1-level], node.Val)
	return
}

func getHeight(node *TreeNode) int {
	if node == nil {
		return 0
	}
	left := getHeight(node.Left)
	right := getHeight(node.Right)
	if left > right {
		return 1 + left
	} else {
		return 1 + right
	}
}
