
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


 function rob(root: TreeNode | null): number {
    let cache = new Map<string, number>()
    return calculate(root, false, cache)
};

function calculate(node: TreeNode | null, previousRob: boolean, cache: Map<string, number>): number {
    if(!node) return 0
    const key = `${JSON.stringify(node)}${previousRob}`
    if(cache.has(key)) {
        return cache.get(key)
    }
    let left = node.left
    let right = node.right
    if(previousRob) {
        cache.set(key, calculate(left, false, cache) + calculate(right, false, cache))
    } else {
        let robThis = node.val + calculate(left, true, cache) + calculate(right, true, cache)
        let passThis = calculate(left, false,cache) + calculate(right, false, cache)
        cache.set(key, Math.max(robThis, passThis))
    }
    return cache.get(key)
}