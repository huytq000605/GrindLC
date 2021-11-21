
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


 function buildTree(inorder: number[], postorder: number[]): TreeNode | null {
    if(inorder.length === 0) {
        return null
    }
    let rootValue = postorder[postorder.length - 1]
    let root = new TreeNode(rootValue)
    let rootIndexInorder = -1
    for(let i = 0; i < inorder.length; i++) {
        if(inorder[i] === rootValue) {
            rootIndexInorder = i
            break
        }
    }
    root.left = buildTree(inorder.slice(0, rootIndexInorder), postorder.slice(0, rootIndexInorder))
    root.right = buildTree(inorder.slice(rootIndexInorder + 1), postorder.slice(rootIndexInorder, postorder.length - 1))
    return root
};
