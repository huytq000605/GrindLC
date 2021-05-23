package main

// Definition for a binary tree node.

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	result := make([][]int, 0)
	helper(root, 0, &result)
	return result

}

// We check the current level, just basic BFS recursion
func helper(node *TreeNode, currentLevel int, result *[][]int) {
	if node == nil {
		return
	}
	if currentLevel+1 > len(*result) {
		*result = append(*result, []int{})
	}
	(*result)[currentLevel] = append((*result)[currentLevel], node.Val)
	helper(node.Left, currentLevel+1, result)
	helper(node.Right, currentLevel+1, result)
}
