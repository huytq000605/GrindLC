
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


 function sufficientSubset(root: TreeNode | null, limit: number): TreeNode | null {
    let sufficientSet = new Set()
    function dfs(node: TreeNode, current, currentSum) {
        if(!node) {
            return
        }
        currentSum += node.val
        current.push(node)
        if(!node.left && !node.right) {
            if(currentSum >= limit) {
                for(let node of current) {
                    sufficientSet.add(node)
                }
            }
        }
        if(node.left) {
            dfs(node.left, current, currentSum)
            current.pop()
        }
        if(node.right) {
            dfs(node.right, current, currentSum)
            current.pop()
        }
    }
    dfs(root, [], 0)
    if(sufficientSet.size === 0) {
        return null
    }
    
    let queue = [root]
    while(queue.length > 0) {
        let current = queue.shift()
        if(sufficientSet.has(current.left)) {
            queue.push(current.left)
        } else {
            current.left = null
        }
        if(sufficientSet.has(current.right)) {
            queue.push(current.right)
        } else {
            current.right = null
        }
    }
    return root
};

