package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func flatten(root *TreeNode) {
	helper(root)
	return
}

/*
Helper function flatten the tree and return the tail
*/
func helper(node *TreeNode) *TreeNode {
	if node == nil {
		return nil
	}
	leftNode := node.Left
	rightNode := node.Right
	left := helper(node.Left)
	right := helper(node.Right)
	node.Left = nil
	if leftNode != nil {
		node.Right = leftNode
		left.Right = rightNode
		if right != nil {
			return right
		} else {
			return left
		}

	} else {
		node.Right = rightNode
		if right != nil {
			return right
		} else {
			return node
		}
	}

}
