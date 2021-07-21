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


 function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
    if(!root) return null
    if(root.val === key) {
        let left = root.left
        let right = root.right
        if(right) {
            root = right
            while(right && right.left) {
                right = right.left
            }
            right.left = left
        } else {
            root = left
        }
        return root
    } else {
        helper(root, null, key)
        return root    
    }
};

function helper(node: TreeNode | null, parent: TreeNode | null, key: number) {
    if(!node) return
    if(node.val === key) {
        let left = node.left
        let right = node.right
        if(right) {
            if(parent.left === node) parent.left = right
            else if(parent.right === node) parent.right = right
            while(right && right.left) {
                right = right.left
            }
            right.left = left
        } else {
            if(parent.left === node) parent.left = left
            else if(parent.right === node) parent.right = left
        }
        
    } else {
        helper(node.left, node, key)
        helper(node.right, node, key)
    }
}