package main

//Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
When picking a node as head, all number < head is on left, and number > head is on the right
*/
func generateTrees(n int) []*TreeNode {
	result := genTree(1, n)
	return result
}

func genTree(start int, end int) []*TreeNode {
	result := make([]*TreeNode, 0)
	if start > end {
		return []*TreeNode{nil} // return a nil node to iterate through it later
	}
	if start == end {
		return []*TreeNode{&TreeNode{Val: start}}
	}

	for i := start; i <= end; i++ {
		lefts := genTree(start, i-1)
		rights := genTree(i+1, end)
		for _, left := range lefts {
			for _, right := range rights {
				head := TreeNode{Val: i}
				head.Left = left
				head.Right = right
				result = append(result, &head)
			}
		}
	}
	return result
}
