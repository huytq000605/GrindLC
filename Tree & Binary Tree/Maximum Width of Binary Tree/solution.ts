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


 function widthOfBinaryTree(root: TreeNode | null): number {
    if(!root) return 0
    let result = 1n
    let queue: any = [[root, 0, 0n]]
    let level = -1
    let min = 0n
    while(queue.length) {
        let [current, currentLevel, position] = queue.shift()
        if(currentLevel === level) {
            if(position - min + 1n > result) {
                result = position - min + 1n
            }
        } else {
            level = currentLevel
            min = position
        }
        if(current.left) queue.push([current.left, currentLevel + 1, position * 2n + 1n])
        if(current.right) queue.push([current.right, currentLevel + 1, position * 2n + 2n])
        
    }
    return Number(result)
};