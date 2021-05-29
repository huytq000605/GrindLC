package main

import (
	"fmt"
	"math"
)

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func printTree(root *TreeNode) [][]string {
	treeHeight := getHeight(root)
	result := make([][]string, treeHeight)
	for i := 0; i < len(result); i++ {
		result[i] = make([]string, int(math.Pow(2, float64(treeHeight)))-1)
	}
	construct(root, 0, 0, int(math.Pow(2, float64(treeHeight)))-1, &result)
	return result
}

func construct(node *TreeNode, level int, start int, end int, result *[][]string) {
	if node == nil {
		return
	}
	index := start + int(math.Floor(float64(end-start)/2))
	(*result)[level][index] = fmt.Sprintf("%v", node.Val)
	construct(node.Left, level+1, start, index, result)
	construct(node.Right, level+1, index, end, result)
}

func getHeight(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftHeight := getHeight(root.Left)
	rightHeight := getHeight(root.Right)
	if leftHeight >= rightHeight {
		return 1 + leftHeight
	} else {
		return 1 + rightHeight
	}
}
