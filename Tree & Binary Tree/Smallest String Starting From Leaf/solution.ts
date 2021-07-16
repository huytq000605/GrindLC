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

 function smallestFromLeaf(root: TreeNode | null): string {
    let result
    function helper(node, current) {
        if(!node) return
        current += String.fromCharCode(node.val + 65 + 32)
        if(!node.left && !node.right) {
            let res = reverse(current)
            if(!result || res.localeCompare(result) === -1) {
                result = res
            }
            return
        }
        helper(node.left, current)
        helper(node.right, current)
    }
    helper(root, "")
    return result
};

function reverse(s) {
    let result = ""
    for(let i = s.length - 1; i >= 0; i--) {
        result += s[i]
    }
    return result
}
