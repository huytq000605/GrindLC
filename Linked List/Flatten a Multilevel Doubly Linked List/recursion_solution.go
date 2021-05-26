package main

// Definition for a Node.
type Node struct {
	Val   int
	Prev  *Node
	Next  *Node
	Child *Node
}

func flatten(root *Node) *Node {
	result, _ := flat(root)
	return result

}

func flat(root *Node) (*Node, *Node) {
	head := root
	var tail *Node
	for root != nil {
		if root.Next == nil && root.Child == nil { // Get tail
			tail = root
		}
		if root.Child == nil {
			root = root.Next
			continue
		} else {
			next := root.Next
			childHead, childTail := flat(root.Child)
			root.Next = childHead
			childHead.Prev = root
			if next != nil {
				childTail.Next = next
				next.Prev = childTail
			} else { // Tail is last child node if no next
				tail = childTail
			}
			root.Child = nil
			root = next
		}

	}
	return head, tail
}
