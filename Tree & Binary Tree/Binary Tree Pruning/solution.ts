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


 function pruneTree(root: TreeNode | null): TreeNode | null {
    if(deleteNode(root)) {
        return null
    }
    return root
    
};

function deleteNode(node: TreeNode) {
    if(!node) return true
    let left = deleteNode(node.left)
    let right = deleteNode(node.right)
    if(left) node.left = null
    if(right) node.right = null
    if(node.val === 0 && left && right) return true
    else return false
    
}