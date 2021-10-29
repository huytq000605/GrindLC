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


 function longestZigZag(root: TreeNode | null): number {
    let result = 0
    let dfs = (node: TreeNode | null, current: number, goLeft: boolean) => {
        if(!node) return
        result = Math.max(result, current)
        if(goLeft) {
			// Continue this route
            dfs(node.left, current + 1, false)
			// count this node, and node.right => current === 1
            dfs(node.right, 1, true)
        } else {
			// Continue this route
            dfs(node.right, current + 1, true)
			// count this node, and node.left => current === 1
            dfs(node.left, 1, false)
        }
    }
    // Go from root, so current = zero
	// goLeft can be either true or false because we will adapt it
    dfs(root, 0, true)
    return result
};