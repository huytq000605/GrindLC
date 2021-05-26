package main

// Definition for a Node.
type Node struct {
	Val   int
	Prev  *Node
	Next  *Node
	Child *Node
}

func flatten(root *Node) *Node {
	head := root
	for root != nil {
		if root.Child == nil {
			root = root.Next
		} else {
			next := root.Next
			child := root.Child
			root.Next = child
			child.Prev = root
			for child.Next != nil {
				child = child.Next
			}
			if next != nil {
				child.Next = next
				next.Prev = child
			}
			root.Child = nil
		}
	}
	return head
}
