package main

//Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type CBTInserter struct {
	root  *TreeNode
	queue []*TreeNode
}

func Constructor(root *TreeNode) CBTInserter {
	result := CBTInserter{
		root: root,
	}
	result.queue = append(result.queue, root)
	for {
		current := result.queue[0]
		q := &result.queue
		if current.Left != nil && current.Right != nil {
			*q = append(*q, current.Left, current.Right)
			*q = (*q)[1:]
		} else {
			break
		}
	}
	return result
}

func (this *CBTInserter) Insert(v int) int {
	current := this.queue[0]
	node := &TreeNode{Val: v}
	if current.Left == nil {
		current.Left = node
	} else {
		current.Right = node
		this.queue = this.queue[1:]
		this.queue = append(this.queue, current.Left, current.Right)
	}
	return current.Val
}

func (this *CBTInserter) Get_root() *TreeNode {
	return this.root
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Insert(v);
 * param_2 := obj.Get_root();
 */
