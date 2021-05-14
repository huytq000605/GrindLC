
//  Definition for a binary tree node.
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
 



 function convertBST(root: TreeNode | null, obj = {sum: 0}): TreeNode | null {
    if(!root) return null
    convertBST(root.right, obj);
    const original = root.val
    root.val += obj.sum;
    obj.sum += original
    convertBST(root.left, obj);
    return root
};
