package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

/*
For O(n) Time complexcity and O(1) space, i hold a firstEven and firstOdd node and an index to notice when its a odd node, then i mark the last odd node
*/
func oddEvenList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	firstEven := head.Next
	firstOdd := head
	lastOdd := head
	idx := 1
	for {
		if head.Next != nil {
			next := head.Next
			head.Next = head.Next.Next
			if idx%2 == 1 { // If current (head) is odd Node, we mark the last odd node
				if head.Next != nil {
					lastOdd = head.Next
				} else {
					lastOdd = head
				}
			}
			head = next
			idx++
		} else {
			break
		}
	}
	lastOdd.Next = firstEven
	return firstOdd
}
