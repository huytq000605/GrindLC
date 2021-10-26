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


 function balanceBST(root: TreeNode | null): TreeNode | null {
    let arr = []
    let dfs = (node) => {
        if(!node) return
        dfs(node.left)
        arr.push(node)
        dfs(node.right)
    }
    dfs(root)
    
    let constructBST = (start: number, end: number) => {
        if(start > end) return null
        let root = start + Math.floor((end - start) / 2)
        arr[root].left = constructBST(start, root - 1)
        arr[root].right = constructBST(root + 1, end)
        return arr[root]
    }
    
    return constructBST(0, arr.length - 1)
    
};