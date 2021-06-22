package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedListToBST(head *ListNode) *TreeNode {
	arr := make([]int, 0)
	for head != nil {
		arr = append(arr, head.Val)
		head = head.Next
	}
	return construct(arr, 0, len(arr)-1)
}

func construct(arr []int, start int, end int) *TreeNode {
	if start > end {
		return nil
	}
	middle := start + (end-start)/2
	node := &TreeNode{Val: arr[middle]}
	node.Left = construct(arr, start, middle-1)
	node.Right = construct(arr, middle+1, end)
	return node
}
