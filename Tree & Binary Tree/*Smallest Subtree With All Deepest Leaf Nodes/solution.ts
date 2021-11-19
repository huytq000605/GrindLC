
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


function subtreeWithAllDeepest(root: TreeNode | null): TreeNode | null {
    return dfs(root)[0]
};

function dfs(root: TreeNode): [TreeNode | null, number] {
    if(!root) return [null, 0]
    const [left, leftLevel] = dfs(root.left);
    const [right, rightLevel] = dfs(root.right);
    if(leftLevel > rightLevel) {
        return [left, leftLevel + 1]
    } else if(leftLevel < rightLevel) {
        return [right, rightLevel + 1]
    } else {
        return [root, leftLevel + 1]
    }
}