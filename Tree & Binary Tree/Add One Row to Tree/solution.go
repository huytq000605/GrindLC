package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
	if depth == 1 {
		head := &TreeNode{Val: val, Left: root}
		return head
	}
	nodeQueue := []*TreeNode{root}
	depthQueue := []int{1}
	for len(nodeQueue) > 0 {
		currentNode := nodeQueue[0]
		currentDepth := depthQueue[0]
		nodeQueue = nodeQueue[1:]
		depthQueue = depthQueue[1:]
		left := currentNode.Left
		right := currentNode.Right
		if currentDepth == depth-1 {
			currentNode.Left = &TreeNode{Val: val, Left: left}
			currentNode.Right = &TreeNode{Val: val, Right: right}
		}
		if currentDepth > depth-1 {
			break
		}
		if left != nil {
			nodeQueue = append(nodeQueue, left)
			depthQueue = append(depthQueue, currentDepth+1)
		}
		if right != nil {
			nodeQueue = append(nodeQueue, right)
			depthQueue = append(depthQueue, currentDepth+1)
		}

	}
	return root
}
