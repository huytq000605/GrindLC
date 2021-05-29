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

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
	let level1 = findLevel(root, p, 0);
    let level2 = findLevel(root,q, 0);
    console.log(level1, level2)
    while(level1 < level2) {
        q = parent(root, q);
        level2--
    }
    while(level1 > level2) {
        p = parent(root, p);
        level1--
    }
    while(p !== q) {
        p = parent(root, p);
        q = parent(root, q);
    }
    return p;
    
};

function findLevel(root, node, level) {
    if(root === node) return level;
    if(!root) return null;
    const result1 = findLevel(root.left, node, level + 1);
    const result2 = findLevel(root.right, node, level +1);
    if(result1) return result1;
    if(result2) return result2;
}

function parent(root, target) {
    if(!root) return null;
    if(root.left === target || root.right === target) return root;
    const rs1 = parent(root.left, target);
    const rs2 = parent(root.right, target);
    if(rs1) return rs1;
    if(rs2) return rs2;
}