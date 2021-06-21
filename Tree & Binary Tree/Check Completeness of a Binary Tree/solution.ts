
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

// If there are any node after null node => not complete

 function isCompleteTree(root: TreeNode | null): boolean {
    if(!root) return false
    let queue = [root]
    let flag = false
    while(queue.length > 0) {
        let current = queue.shift()
        if(flag) {
            if(current) return false
            continue
        }
        if(!current) {
            flag = true
            continue
        }
        queue.push(current.left)
        queue.push(current.right)
    }
    return true
    
    
};