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
/*
For people who are curious about why in-order doesn't work, here's a simple example:
TreeA:
0
/
0

TreeB:
0
\
0

They both have same in-order serialization "#0#0#" if we just use "#" to represent null.
*/


 function findDuplicateSubtrees(root: TreeNode | null): Array<TreeNode | null> {
    let seen = new Map()
    let result = []
    let dfs = (current) => {
        if(!current) return ""
        let left = dfs(current.left)
        let right = dfs(current.right)
        
        let tree = `${current.val}#${left}#${right}` // Cannot let the tree string by inorder, can make dupplicate
        if(seen.has(tree) && seen.get(tree) === false) {
            seen.set(tree, true)
            result.push(current)
        }
        if(!seen.has(tree)) {
            seen.set(tree, false)
        }
        return tree
    }
    dfs(root)
    return result
    
};