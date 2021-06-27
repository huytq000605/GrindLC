package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func btreeGameWinningMove(root *TreeNode, n int, x int) bool {
	xNode := findXNode(root, x)
	countLeft := countNode(xNode.Left)
	countRight := countNode(xNode.Right)
	if 2*(countLeft+countRight+1) < n || 2*countLeft > n || 2*countRight > n {
		return true
	}
	return false
}

func findXNode(node *TreeNode, value int) *TreeNode {
	if node == nil {
		return nil
	}
	if node.Val == value {
		return node
	}
	findLeft := findXNode(node.Left, value)
	if findLeft != nil {
		return findLeft
	}
	findRight := findXNode(node.Right, value)
	return findRight
}

func countNode(node *TreeNode) int {
	if node == nil {
		return 0
	}
	return 1 + countNode(node.Left) + countNode(node.Right)
}
