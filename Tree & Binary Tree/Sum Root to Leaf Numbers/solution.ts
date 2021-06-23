
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
    if(!root) {
        return 0
    }
    if(root.val === 0) {
        return sumNumbers(root.left) + sumNumbers(root.right)
    }
    let numbers = []
    let sum = 0
    helper(root, "", numbers)
    for(let num of numbers) {
        sum += num
    }
    return sum
};

function helper(node: TreeNode | null, current: string, numbers: Array<number>) {
	if(!node) return
    current += node.val
    if(!node.left && !node.right) {
        numbers.push(Number(current))
        return
    }
	helper(node.left, current, numbers);
	helper(node.right, current, numbers);
}