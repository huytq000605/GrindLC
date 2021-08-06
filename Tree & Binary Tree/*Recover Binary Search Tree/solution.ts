
// Definition for a binary tree node.
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

/**
 Do not return anything, modify root in-place instead.
 */
/*
**: Inorder traversal in BST give us a sort asc traversal
Because we have only 2 wrong node, so to find the first one, we just need to do inorder traversal and see if we got an node that > prev => that prev is the first one, and current node maybe the second, but we need to keep update the second to find the last one to swap
*/
 function recoverTree(root: TreeNode | null): void {
    let first = null
    let second = null
    let prev = new TreeNode(Number.MIN_SAFE_INTEGER)
    let inOrderTraversal = (node) => {
        if(!node) return
        
        inOrderTraversal(node.left)
        
        if(!first && node.val < prev.val) {
            first = prev
        }
        
        if(first && node.val < prev.val) {
            second = node
        }
        
        prev = node
        
        inOrderTraversal(node.right)
    }
    inOrderTraversal(root);
    [first.val, second.val] = [second.val, first.val]
}
