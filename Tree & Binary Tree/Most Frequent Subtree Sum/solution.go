package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findFrequentTreeSum(root *TreeNode) []int {
	hashmap := make(map[int]int)
	highestFrequent := 1
	helper(root, &hashmap, &highestFrequent)
	result := []int{}
	for key, value := range hashmap {
		if value == highestFrequent {
			result = append(result, key)
		}
	}
	return result
}

func helper(node *TreeNode, hashmap *map[int]int, highestFrequent *int) int {
	if node == nil {
		return 0
	}
	leftSum := helper(node.Left, hashmap, highestFrequent)
	rightSum := helper(node.Right, hashmap, highestFrequent)
	key := leftSum + rightSum + node.Val
	if value, ok := (*hashmap)[key]; !ok {
		(*hashmap)[key] = 1
	} else {
		(*hashmap)[key] = value + 1
		if value+1 > *highestFrequent {
			*highestFrequent = value + 1
		}
	}
	return key

}
