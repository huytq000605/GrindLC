package main

// Definition for a Node.
type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

type QueueNode []interface{}

func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	queue := []QueueNode{QueueNode{root, 0}}
	for len(queue) > 0 {
		currentNode, currentLevel := queue[0][0].(*Node), queue[0][1].(int)
		queue = queue[1:]
		nextNode, nextLevel := &Node{}, -1
		if len(queue) > 0 {
			nextNode = queue[0][0].(*Node)
			nextLevel = queue[0][1].(int)
		}
		if currentLevel == nextLevel {
			currentNode.Next = nextNode
		}
		if currentNode.Left != nil {
			queue = append(queue, QueueNode{currentNode.Left, currentLevel + 1})
		}
		if currentNode.Right != nil {
			queue = append(queue, QueueNode{currentNode.Right, currentLevel + 1})
		}
	}
	return root
}
