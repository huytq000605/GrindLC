
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
    function construct(inorderStart: number, postorderStart: number, postorderEnd: number) {
        if(postorderStart > postorderEnd || inorderStart >= inorder.length) {
            return null
        }
        
        let rootValue = postorder[postorderEnd]
        let root = new TreeNode(rootValue)
        let rootIndexInorder = -1
        for(let i = inorderStart; i <= inorder.length; i++) {
            if(inorder[i] === rootValue) {
                rootIndexInorder = i
                break
            }
        }
        root.left = construct(inorderStart, postorderStart, postorderStart + (rootIndexInorder - inorderStart) - 1)
        root.right = construct(rootIndexInorder + 1, postorderStart + (rootIndexInorder - inorderStart), postorderEnd - 1)
        return root
    }
    return construct(0, 0, postorder.length - 1)
    
};


