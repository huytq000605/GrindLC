
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


 function pathSum(root: TreeNode | null, targetSum: number): number[][] {
    let result = []
    function dfs(node: TreeNode | null, currentSum: number, current: number[]) {
        if(!node) {
            return
        }
        currentSum += node.val
        current.push(node.val)
        if(currentSum === targetSum && !node.left && !node.right) {
            result.push([...current])
            return
        }
        if(node.left) {
            dfs(node.left, currentSum, current)
            current.pop()
        }
        if(node.right) {
            dfs(node.right, currentSum, current)
            current.pop()
        }
    }
    dfs(root, 0, [])
    return result
};
