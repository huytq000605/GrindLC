
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
    let height = getHeight(root)
    if(height === 1) {
        return 1
    }
    if(getHeight(root.right) === height - 1) {
        return 1 + (1 << (height - 1)) - 1 + countNodes(root.right)
    } else {
        return 1 + countNodes(root.left) + (1 << (height - 2)) - 1
    }
};

function getHeight(node: TreeNode) {
    if(!node) return 0
    return 1 + getHeight(node.left)
}