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


function trimBST(root: TreeNode | null, low: number, high: number): TreeNode | null {
	if(!root) return null;
	let left = trimBST(root.left, low, high);
	let right = trimBST(root.right, low, high);
	if(root.val > high) {
		return left
	}
	if(root.val < low) {
		return right
	} 
	root.left = left
	root.right = right
	return root;
};