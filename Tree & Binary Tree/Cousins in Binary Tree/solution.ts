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


function isCousins(root: TreeNode | null, x: number, y: number): boolean {
    let xLevel = -1
    let yLevel = -1
    let dfs = (current, level) => {
        if(!current) return true
        if(current.left && current.right) { // If x and y has same parent
            if((current.left.val === x && current.right.val === y) || (current.right.val === x && current.left.val === y)) return false
        }
        if(current.val === x) { // Found x
            xLevel = level
            return true
        }
        if(current.val === y) { // Found y
            yLevel = level
            return true
        }
        return dfs(current.left, level + 1) && dfs(current.right, level + 1) // If a node is parent of both x and y then return false
    }
    if(!dfs(root, 0)) return false // x and y has same parent
    if(xLevel === -1 || yLevel === -1 || xLevel !== yLevel) return false // Not found x, y or x and y don't have same level
    return true
};