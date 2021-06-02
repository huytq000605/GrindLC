package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findFrequentTreeSum(root *TreeNode) []int {
	freqMap := make(map[int]int)
	helper(root, freqMap)
	highestFreq := 0
	result := make([]int, 0)
	for _, value := range freqMap {
		if value > highestFreq {
			highestFreq = value
		}
	}
	for key, value := range freqMap {
		if value == highestFreq {
			result = append(result, key)
		}
	}
	return result
}

func helper(node *TreeNode, freq map[int]int) int {
	if node == nil {
		return 0
	}
	left := helper(node.Left, freq)
	right := helper(node.Right, freq)
	key := left + right + node.Val
	freq[key] = freq[key] + 1
	return key
}
