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


function sumNumbers(root: TreeNode | null): number {
    let result = 0;
    let dfs = (node: TreeNode | null, current: number) => {
        if (!node) return;
        current = current * 10 + node.val;
        if (!node.left && !node.right) result += current;
        else {
            dfs(node.left, current);
            dfs(node.right, current);
        }
    };
    dfs(root, 0);
    return result;
 };