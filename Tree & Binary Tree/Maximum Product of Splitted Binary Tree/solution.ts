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


 function maxProduct(root: TreeNode | null): number {
    let cache = new Map()
    let dfs = (current) => {
        if(!current) return 0
        if(cache.has(current)) return cache.get(current)
        let result = current.val
        result += dfs(current.left)
        result += dfs(current.right)
        cache.set(current, result)
        return result
    }
    let result = Number.MIN_SAFE_INTEGER
    let sum = dfs(root)
    let queue = [root]
    let MOD = 1e9 + 7
    while(queue.length) {
        let current = queue.shift()
        let secondSum = dfs(current)
        result = Math.max(result, (sum-secondSum) * secondSum)
        if(current.left) queue.push(current.left)
        if(current.right) queue.push(current.right)
    }
    return result % MOD
};