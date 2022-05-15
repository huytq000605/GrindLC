/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

 function deepestLeavesSum(root: TreeNode | null): number {
	const maxLevel = findMaxLevel(root);
	return deepestSum(root, maxLevel, 1);
};

function findMaxLevel(root: TreeNode): number {
	if(!root) return 0;
	return 1 + Math.max(findMaxLevel(root.left), findMaxLevel(root.right));
}

function deepestSum(root: TreeNode | null, maxLevel: number, currentLevel: number) {
	if(!root) return 0;
	let sum = 0;
	if(currentLevel === maxLevel && !root.left && !root.right) {
			sum += root.val;
	}
	sum+= deepestSum(root.left, maxLevel, currentLevel+1);
	sum+= deepestSum(root.right, maxLevel, currentLevel +1);
	return sum;
	
}