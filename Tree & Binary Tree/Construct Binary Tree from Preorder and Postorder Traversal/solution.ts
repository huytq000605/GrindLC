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

 function constructFromPrePost(preorder: number[], postorder: number[]): TreeNode | null {
    if(!preorder.length) return null
    let root = new TreeNode(preorder[0])
    if(preorder.length === 1) return root
    let leftNodes = postorder.indexOf(preorder[1]) + 1
    root.left = constructFromPrePost(preorder.slice(1, 1 + leftNodes), postorder.slice(0, leftNodes))
    root.right = constructFromPrePost(preorder.slice(1 + leftNodes), postorder.slice(leftNodes, postorder.length - 1))
    return root
};