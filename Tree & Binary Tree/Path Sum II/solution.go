package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, targetSum int) [][]int {
	result := make([][]int, 0)
	current := make([]int, 0)
	dfs(root, 0, &current, &result, targetSum)
	return result
}

func dfs(node *TreeNode, currentSum int, current *[]int, result *[][]int, target int) {
	if node == nil {
		return
	}
	currentSum += node.Val
	*current = append(*current, node.Val)
	if currentSum == target && node.Left == nil && node.Right == nil {
		bePushed := make([]int, 0)
		bePushed = append(bePushed, (*current)...)
		*result = append(*result, bePushed)
		return
	}
	if node.Left != nil {
		dfs(node.Left, currentSum, current, result, target)
		*current = (*current)[:len(*current)-1]
	}
	if node.Right != nil {
		dfs(node.Right, currentSum, current, result, target)
		*current = (*current)[:len(*current)-1]
	}

}
