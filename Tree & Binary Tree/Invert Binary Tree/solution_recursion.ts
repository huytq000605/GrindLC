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


 function invertTree(root: TreeNode | null): TreeNode | null {
    let dfs = (node) => {
        if(!node) return
        [node.left, node.right] = [node.right, node.left]
        dfs(node.left)
        dfs(node.right)
    }
    dfs(root)
    return root
};