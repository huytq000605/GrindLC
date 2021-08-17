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


 function goodNodes(root: TreeNode | null): number {
    let result = 0
    let dfs = (current: TreeNode | null, max: number) => {
        if (!current) return;
        if (current.val >= max) result++;
        max = Math.max(current.val, max);
        dfs(current.left, max);
        dfs(current.right, max);
    }; 
    dfs(root, Number.MIN_SAFE_INTEGER)
    return result
};