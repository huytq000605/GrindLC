
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


function rightSideView(root: TreeNode | null): number[] {
    let result = [];
    helper(root, 0, result);
    return result
};


function helper(node: TreeNode | null, level: number, result: number[]) {
    if(!node) return;
    result[level] = node.val
    helper(node.left, level + 1, result);
    helper(node.right, level + 1, result);
    return;
}