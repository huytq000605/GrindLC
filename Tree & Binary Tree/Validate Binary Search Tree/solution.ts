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


 function isValidBST(root: TreeNode | null): boolean {
    let min = Number.MIN_SAFE_INTEGER
    let traversal = (current) => {
        if(!current) return true
        if(!traversal(current.left)) return false
        if(current.val <= min) {
            return false
        }
        min = current.val
        if(!traversal(current.right)) return false
        return true
    }
    return traversal(root)
};