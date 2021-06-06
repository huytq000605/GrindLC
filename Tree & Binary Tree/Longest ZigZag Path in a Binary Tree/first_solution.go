package main

import "fmt"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestZigZag(root *TreeNode) int {
	memo := make(map[string]int) // Create a map for memoization
	return longestZigZagWithHead(root, memo)
}

func longestZigZagWithHead(node *TreeNode, memo map[string]int) int {
	if node == nil {
		return 0
	}
	goLeft := traversal(node, true, memo)            // go Left from this node
	goRight := traversal(node, false, memo)          // go right from this node
	left := longestZigZagWithHead(node.Left, memo)   // go to the left as starting point
	right := longestZigZagWithHead(node.Right, memo) // go to the right as starting point
	return max(goLeft, goRight, left, right)
}

func traversal(node *TreeNode, left bool, memo map[string]int) int {
	if node == nil { // -1 because we need how many left/right
		return -1
	}
	key := fmt.Sprintf("%v%v", node, left) // Key is adress of node and direction left/right
	if res, ok := memo[key]; ok {
		return res
	}
	if left { // We are counting the node/ height
		memo[key] = 1 + traversal(node.Left, false, memo)
		return memo[key]
	} else {
		memo[key] = 1 + traversal(node.Right, true, memo)
		return memo[key]
	}
}

func max(arr ...int) int { // Math.max
	result := arr[0]
	for i := 0; i < len(arr); i++ {
		if arr[i] > result {
			result = arr[i]
		}
	}
	return result
}
