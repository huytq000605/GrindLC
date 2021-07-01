package main

// Definition for a binary tree node.

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getHeight(this *TreeNode) int {
	if this == nil {
		return 0
	}
	return 1 + getHeight(this.Left)
}

func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}
	height := getHeight(root)
	rightHeight := getHeight(root.Right)
	if rightHeight == height-1 {
		return 1 + (1 << (height - 1)) - 1 + countNodes(root.Right)
	} else {
		return 1 + (countNodes(root.Left)) + (1 << rightHeight) - 1
	}
}
