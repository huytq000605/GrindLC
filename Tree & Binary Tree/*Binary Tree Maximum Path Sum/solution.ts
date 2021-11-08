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


 function maxPathSum(root: TreeNode | null): number {
    let result = Number.MIN_SAFE_INTEGER
    let dfs = (node) => {
        if(!node) return 0
        let current = node.val
        let left = dfs(node.left)
        let right = dfs(node.right)
        result = Math.max(result, left + current, right + current, current, left + current + right)
        return Math.max(current + left, current, current + right)
    }
    dfs(root)
    return result
};