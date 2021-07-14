
// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


 function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let root = new ListNode()
    let current = root
    while(l1 && l2) {
        current.val += l1.val + l2.val
        if(current.val >= 10) {
            current.val = current.val % 10
            current.next = new ListNode(1)
        } else {
            if(l1.next || l2.next)
            current.next = new ListNode(0)
        }
        current = current.next
        l1 = l1.next
        l2 = l2.next
    }
    while(l1) {
        current.val += l1.val
        if(current.val >= 10) {
            current.val = current.val % 10
            current.next = new ListNode(1)
        } else {
            if(l1.next)
            current.next = new ListNode(0)
        }
        current = current.next
        l1 = l1.next
    }
    while(l2) {
        current.val += l2.val
        if(current.val >= 10) {
            current.val = current.val % 10
            current.next = new ListNode(1)
        } else {
            if(l2.next)
            current.next = new ListNode(0)
        }
        current = current.next
        l2 = l2.next
    }
    return root
};