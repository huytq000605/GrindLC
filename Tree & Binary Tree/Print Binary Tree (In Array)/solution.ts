
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


function printTree(root: TreeNode | null): string[][] {
    const height = getHeight(root);
    let result = Array(height).fill(0).map(e => Array(Math.pow(2, height) - 1).fill(""))
    construct(root, 0, 0, Math.pow(2, height) - 1, result)
    return result;
};

function construct(node: TreeNode, level: number, start: number, end: number, result: string[][]) {
    if(!node) return
    let idx = Math.floor(start + (end-start)/2)
    result[level][idx] = node.val.toString()
    construct(node.left, level + 1, start, idx, result)
    construct(node.right, level + 1, idx, end, result)
}

function getHeight(root: TreeNode) {
    if(!root) {
        return 0
    }
    return 1 + Math.max(getHeight(root.left), getHeight(root.right))
} 