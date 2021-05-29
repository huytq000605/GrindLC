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

function subtreeWithAllDeepest(root: TreeNode | null): TreeNode | null {
    return helper(root, 0)[0]
};

function helper(root, level) {
    if(!root.left && !root.right) return [root,level]
    if(!root.left) return helper(root.right, level + 1)
    if(!root.right) return helper(root.left, level + 1)
    const r1 = helper(root.left, level + 1);
    const r2 = helper(root.right, level + 1);
    if(r1[1] > r2[1]) return r1
    else if(r1[1] < r2[1]) return r2
    else return [root, r1[1]]
}