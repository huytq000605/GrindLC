/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

 function diameterOfBinaryTree(root: TreeNode | null): number {
    let result = 0
    let maxDepth = (node) => {
        if(!node) return 0
        let left = maxDepth(node.left)
        let right = maxDepth(node.right)
        result = Math.max(result, left + right)
        return Math.max(left, right) + 1
    }
    maxDepth(root)
    return result
};