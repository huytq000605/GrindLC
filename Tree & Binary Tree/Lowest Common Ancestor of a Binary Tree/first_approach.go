package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	levelP := getHeight(root, p, 0)
	levelQ := getHeight(root, q, 0)
	for levelP > levelQ {
		p = getParent(root, p)
		levelP--
	}
	for levelQ > levelP {
		q = getParent(root, q)
		levelQ--
	}
	for p != q {
		p = getParent(root, p)
		q = getParent(root, q)
	}
	return p
}

func getHeight(current *TreeNode, target *TreeNode, level int) int {
	if current == nil {
		return 0
	}
	if current == target {
		return level
	}
	left := getHeight(current.Left, target, level+1)
	right := getHeight(current.Right, target, level+1)
	if left != 0 {
		return left
	} else {
		return right
	}
}

func getParent(current *TreeNode, target *TreeNode) *TreeNode {
	if current == nil {
		return nil
	}
	if current.Left == target || current.Right == target {
		return current
	}
	left := getParent(current.Left, target)
	right := getParent(current.Right, target)
	if left != nil {
		return left
	} else {
		return right
	}
}
