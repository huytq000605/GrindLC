
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


 function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    function construct(preorderStart, inorderStart, inorderEnd) {
        if(inorderStart > inorderEnd || preorderStart >= preorder.length) {
            return null
        }
        let rootValue = preorder[preorderStart]
        let root = new TreeNode(rootValue)
        let inorderIndex = -1
        for(let i = inorderStart; i <= inorderEnd; i++) {
            if(inorder[i] === rootValue) {
                inorderIndex = i
                break
            }
        }
        root.left = construct(preorderStart + 1, inorderStart, inorderIndex - 1)
        root.right = construct(preorderStart + inorderIndex - inorderStart + 1, inorderIndex + 1, inorderEnd)
        return root
    }
    return construct(0, 0, inorder.length - 1)
};