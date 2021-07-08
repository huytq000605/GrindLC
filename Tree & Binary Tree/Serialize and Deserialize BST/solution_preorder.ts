
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


/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
    if(!root) return ""
    let result = ""
    function dfs(node: TreeNode) {
        if(!node) {
            result += "#,"
        } else {
            result += node.val + ","
            dfs(node.left)
            dfs(node.right)
        }
    }
    dfs(root)
    return result.slice(0, result.length - 1)
};

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
    if(data === "") return null
    let arr = data.split(",")
    let root = new TreeNode(Number(arr[0]))
    let index = 1
    function dfs(node: TreeNode) {
        if(index >= arr.length) return
        if(arr[index] !== "#") {
            node.left = new TreeNode(Number(arr[index]))
            index++
            dfs(node.left)
            
        }
        index++
        if(index >= arr.length) return
        if(arr[index] !== "#") {
            node.right = new TreeNode(Number(arr[index]))
            index++
            dfs(node.right)
        }
    }
    dfs(root)
    return root
};


/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */