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


 function isEvenOddTree(root: TreeNode | null): boolean {
    let level = 0
    let value = 0
    let queue: [TreeNode, number][] = [[root, 0]]
    while(queue.length) {
        let [currentNode, currentLevel] = queue.shift()
        if(currentLevel !== level) {
            value = 0
            level = currentLevel
        }
        let isEvenLevel = currentLevel % 2 === 0 ? true : false
        if(isEvenLevel) {
            if(currentNode.val % 2 === 0) {
                return false
            }
            if(value !== 0 && currentNode.val <= value) {
                return false
            }
        } else {
            if(currentNode.val % 2 === 1) {
                return false
            }
            if(value !== 0 && currentNode.val >= value) {
                return false
            }
        }
        if(currentNode.left) queue.push([currentNode.left, currentLevel + 1])
        if(currentNode.right) queue.push([currentNode.right, currentLevel + 1])
        value = currentNode.val
    }
    return true
};