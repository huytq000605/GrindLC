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


 function longestUnivaluePath(root: TreeNode | null): number {
    let numOfNodes = 1
    let dfs = (current) => {
        if(!current) return 0
        let left = dfs(current.left)
        let right = dfs(current.right)
        if(current.left && current.left.val !== current.val) {
            left = 0
        }
        if(current.right && current.right.val !== current.val) {
            right = 0
        }
        numOfNodes = Math.max(numOfNodes, 1 + left + right) // This is starting point so can go both left and right
        return Math.max(left, right) + 1 // return only left or right
    }
    dfs(root)
    return numOfNodes - 1
};