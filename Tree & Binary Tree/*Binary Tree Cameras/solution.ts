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


// Greedy problem
// Just go from leaf to leave by post order, mark status, 2 is filled by others, 1 is filled by itself, 0 is not filled yet

 function minCameraCover(root: TreeNode | null): number {
    let result = 0
    let dfs = (current) => {
        if(!current) return 2
        let left = dfs(current.left)
        let right = dfs(current.right)
        if(left === 0 || right === 0) {
            result++
            return 1
        }
        if(left === 1 || right === 1) return 2
        return 0
    }
    if(!root) return 0
    if(dfs(root) === 0) result++  // if root is not filled, then filled itself
    return result
};