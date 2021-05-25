package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func nextLargerNodes(head *ListNode) []int {
	list := make([]int, 0)
	for head != nil {
		list = append(list, head.Val)
		head = head.Next
	}
	result := make([]int, len(list))
	stack := make([]int, 0)
	for i, ele := range list {
		for len(stack) > 0 && list[stack[len(stack)-1]] < ele {
			idx := stack[len(stack)-1]
			result[idx] = ele
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}
	return result

}
