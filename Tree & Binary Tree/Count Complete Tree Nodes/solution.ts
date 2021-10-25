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


 function countNodes(root: TreeNode | null): number {
    if(!root) return 0
    let leftLevel = getHeight(root.left)
    let rightLevel = getHeight(root.right)
    if(leftLevel > rightLevel) {
        return countNodes(root.left) + (1 << rightLevel)
    } else {
        return (1 << rightLevel) + countNodes(root.right)
    }
    
};

function getHeight(root) {
    if(!root) return 0
    return getHeight(root.left) + 1
}