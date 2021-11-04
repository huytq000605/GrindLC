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


 function sumOfLeftLeaves(root: TreeNode | null): number {
    let result = 0
    let dfs = (node: TreeNode | null, parentGoLeft: boolean) => {
        if(!node) return
        if(!node.left && !node.right && parentGoLeft) {
            result += node.val 
        }
        dfs(node.left, true)
        dfs(node.right, false)
    }
    dfs(root, false)
    return result
};