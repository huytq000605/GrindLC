package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	var firstNode *ListNode
	if head.Next == nil {
		return head
	} else {
		firstNode = head.Next
	}

	var prev *ListNode
	for head != nil {
		node1 := head
		node2 := head.Next
		var next *ListNode
		if node2 != nil {
			next = node2.Next
			node2.Next = node1
		}
		if prev != nil && node2 != nil {
			prev.Next = node2
		}
		node1.Next = next
		head = next
		prev = node1
	}
	return firstNode

}
