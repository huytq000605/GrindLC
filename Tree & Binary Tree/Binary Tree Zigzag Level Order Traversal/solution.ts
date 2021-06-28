
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


 function zigzagLevelOrder(root: TreeNode | null): number[][] {
    if(!root) {
        return []
    }
    let fromLeftToRight = true
    let previousLevel = 0;
    let queue: any = [[root, 0]]
    
    let result = [[]]
    while(queue.length) {
        let [currentNode, currentLevel] = queue.shift()
        if(previousLevel !== currentLevel) {
            fromLeftToRight = !fromLeftToRight
            result.push([])
        }
        if(fromLeftToRight) {
            result[currentLevel].push(currentNode.val)
        } else {
            result[currentLevel].unshift(currentNode.val)
        }
        if(currentNode.left) queue.push([currentNode.left, currentLevel + 1])
        if(currentNode.right) queue.push([currentNode.right, currentLevel + 1])
        previousLevel = currentLevel
        
    }
    return result
};