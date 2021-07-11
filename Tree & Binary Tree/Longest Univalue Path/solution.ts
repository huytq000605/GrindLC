
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


 function longestUnivaluePath(node: TreeNode | null): number {
    if(!node) return 0
    let result = 1
    if(node.left && node.left.val === node.val) {
        result += helper(node.left)
    } 
    if(node.right && node.right.val === node.val) {
        result += helper(node.right)
    }
    let left = longestUnivaluePath(node.left)
    let right = longestUnivaluePath(node.right)
    return Math.max(left, right, result - 1) // Each start have two ways to go down, -1 because result is number of nodes
};

function helper(node: TreeNode) {
    let left = 0
    let right = 0
    if(node.left && node.left.val === node.val) {
        left = helper(node.left)
    }
    if(node.right && node.right.val === node.val) {
        right = helper(node.right)
    }
    return Math.max(1 + left, 1 + right)
    
}