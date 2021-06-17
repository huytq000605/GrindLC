package main

import "fmt"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	result := make([]*TreeNode, 0)
	seen := make(map[string]bool)
	postOrder(root, &result, seen)
	return result
}

func postOrder(node *TreeNode, result *[]*TreeNode, seen map[string]bool) string {
	if node == nil {
		return "#"
	}
	left := postOrder(node.Left, result, seen)
	right := postOrder(node.Right, result, seen)
	key := fmt.Sprintf("%v-%v-%v", node.Val, left, right)
	if value, ok := seen[key]; ok {
		if value == false {
			*result = append(*result, node)
			seen[key] = true
		}
	} else {
		seen[key] = false
	}
	return key
}
