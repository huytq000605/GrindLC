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
// Because voyage.length = num of Tree Node so we dont need to check for length

 function flipMatchVoyage(root: TreeNode | null, voyage: number[]): number[] {
    let result = []
    let index = 0
    // We traversal through the tree by preorder just like the voyage and see
    function dfs(node: TreeNode | null) {
        if(!node) return true
        if(node.val !== voyage[index]) return false
        index++
        if(node.left) {
            if(node.left.val === voyage[index]) {
                return dfs(node.left) && dfs(node.right)
            } else {
                result.push(node.val)
                return dfs(node.right) && dfs(node.left)
            }
        }
        return dfs(node.right)
    }
    if(!dfs(root)) return [-1]
    return result
};