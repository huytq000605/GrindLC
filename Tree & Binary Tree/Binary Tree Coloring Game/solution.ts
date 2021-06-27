
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


 function btreeGameWinningMove(root: TreeNode | null, n: number, x: number): boolean {
    let XNode = findXNode(root, x)
    let left = countTreeNode(XNode.left)
    let right = countTreeNode(XNode.right)
    let numOfXNode = countTreeNode(XNode)
    if(n - numOfXNode > numOfXNode || left > n - left || right > n- right) {
        return true
    }
    return false
};

function countTreeNode(node: TreeNode): number {
    if(!node) return 0
    return 1 + countTreeNode(node.left) + countTreeNode(node.right)
}

function findXNode(node: TreeNode, value: number): TreeNode | null {
    if(!node) return null
    if(node.val === value) {
        return node
    }
    return findXNode(node.left, value) || findXNode(node.right, value)
    
}