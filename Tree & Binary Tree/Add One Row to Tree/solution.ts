
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


 function addOneRow(root: TreeNode | null, val: number, depth: number): TreeNode | null {
    if(depth === 1) {
        let head = new TreeNode(val, root)
        return head;
    }
    let queue: Array<[TreeNode | null, number]> = [[root, 1]]
    while(queue.length) {
        let [currentNode, currentDepth] = queue.shift()
        let left = currentNode.left
        let right = currentNode.right
        if(currentDepth === depth - 1) {
            currentNode.left = new TreeNode(val, left)
            currentNode.right = new TreeNode(val, null, right)
        }
        if(currentDepth > depth - 1) break;
        if(left) queue.push([left, currentDepth + 1])
        if(right) queue.push([right, currentDepth + 1])
    }
    return root
};