
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


 function pathSum(root: TreeNode | null, targetSum: number): number {
    let cache = new Map()
    cache.set(0 , 1)
    return helper(root, 0, targetSum, cache)
};

function helper(node: TreeNode | null, currentSum: number, target: number, cache: Map<number, number>) {
    if(!node) return 0
    let result = 0
    currentSum += node.val
    if(cache.has(currentSum - target)) { // Prefix array so can find sum of any subarray = target
        result += cache.get(currentSum - target)
    }
    cache.set(currentSum, (cache.get(currentSum) || 0)  + 1)
    result += helper(node.left, currentSum, target, cache)
    result += helper(node.right, currentSum, target, cache)
    cache.set(currentSum, cache.get(currentSum) - 1)
    return result
    
}

