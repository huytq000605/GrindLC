
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


function findDuplicateSubtrees(root: TreeNode | null): Array<TreeNode | null> {
    let result = []
    let seen = new Map()
    postOrder(root, result, seen)
    return result
};


function postOrder(node : TreeNode | null, result, seen): string {
    if(!node) {
        return "#"
    }
    let left = postOrder(node.left, result, seen)
    let right = postOrder(node.right, result, seen)
    const key = `${node.val}-${left}-${right}`
    if(seen.has(key)) {
        if(seen.get(key) === false) {
            result.push(node)
            seen.set(key, true)
        }     
    } else {
        seen.set(key, false)
    }
    return key
}