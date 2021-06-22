
// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}



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


 function sortedListToBST(head: ListNode | null): TreeNode | null {
    let nodeArr = []
    while(head) {
        nodeArr.push(head.val)
        head = head.next
    }
    return constructBST(nodeArr, 0, nodeArr.length - 1)
    
};

function constructBST(arr, start, end) {
    if(start > end) {
        return null
    }
    let middle = start + Math.floor((end-start)/ 2)
    let node = new TreeNode(arr[middle])
    node.left = constructBST(arr, start, middle- 1)
    node.right = constructBST(arr, middle + 1, end)
    return node
}