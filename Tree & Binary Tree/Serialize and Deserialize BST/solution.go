package main

import (
	"strconv"
	"strings"
)

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	queue := []*TreeNode{root}
	result := ""
	for len(queue) > 0 {
		current := queue[0]
		if current != nil {
			result += strconv.Itoa(current.Val)
			result += ","
			queue = append(queue, current.Left, current.Right)
		} else {
			result += "-1,"
		}
		queue = queue[1:]
	}
	return result[:len(result)-1]
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	nodeArrayAsString := strings.Split(data, ",")
	nodeArray := make([]int, len(nodeArrayAsString))
	for i := 0; i < len(nodeArray); i++ {
		nodeArray[i], _ = strconv.Atoi(nodeArrayAsString[i])
	}
	var result *TreeNode
	if len(nodeArray) == 0 || nodeArray[0] == -1 {
		return result
	}
	result = &TreeNode{Val: nodeArray[0]}
	queue := []*TreeNode{result}
	index := 1
	for index < len(nodeArray) {
		current := queue[0]
		if nodeArray[index] != -1 {
			current.Left = &TreeNode{Val: nodeArray[index]}
			queue = append(queue, current.Left)
		} else {
			current.Left = nil
		}

		index++
		if index == len(nodeArray) {
			return result
		}
		if nodeArray[index] != -1 {
			current.Right = &TreeNode{Val: nodeArray[index]}
			queue = append(queue, current.Right)
		} else {
			current.Right = nil
		}
		index++
		queue = queue[1:]
	}
	return result
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor()
 * deser := Constructor()
 * tree := ser.serialize(root)
 * ans := deser.deserialize(tree)
 * return ans
 */
