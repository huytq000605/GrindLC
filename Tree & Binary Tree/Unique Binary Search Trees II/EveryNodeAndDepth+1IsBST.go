package main

//Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func generateTrees(n int) []*TreeNode {
	result := make([]*TreeNode, 0)
	nums := make([]int, n)
	for i := range nums {
		nums[i] = i + 1
	}
	for i := 0; i < len(nums); i++ {
		remaining := append(append([]int{}, nums[:i]...), nums[i+1:]...)
		trees := helper(i+1, remaining)
		result = append(result, trees...)
	}
	return result
}

func helper(headValue int, remaining []int) []*TreeNode {
	result := make([]*TreeNode, 0)
	if len(remaining) == 0 {
		return []*TreeNode{&TreeNode{Val: headValue}}
	}
	for idx, nextNodeValue := range remaining {
		nextRemaining := append(append([]int{}, remaining[:idx]...), remaining[idx+1:]...)
		nexts := helper(nextNodeValue, nextRemaining)
		for _, next := range nexts {
			head := TreeNode{Val: headValue}
			if nextNodeValue < headValue {
				head.Left = next
			} else {
				head.Right = next
			}
			result = append(result, &head)
		}
	}
	return result
}
