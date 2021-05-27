package main

// Definition for a binary tree node.
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

/*
From the right side PoV, so for each level of tree, we can see 1 node on the rightest
We can traversal BFS, left first then right, then the node after will be the node we see
*/

 func rightSideView(root *TreeNode) []int {
    result := make([]int, 0)
    helper(root, 0, &result)
    return result;
}

func helper(node *TreeNode, level int, result *[]int) {
    if node == nil {
        return
    }
    if len(*result) < level + 1 {
        *result = append(*result, node.Val)
    } else {
        (*result)[level] = node.Val
    } 
    helper(node.Left, level + 1, result)
    helper(node.Right, level + 1, result)
    
    return
}