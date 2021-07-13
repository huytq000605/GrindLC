
// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


 function sortList(head: ListNode | null): ListNode | null {
    if(!head) return null
    if(!head.next) {
        return head
    }
    let prev = null
    let slow = head
    let fast = head
    while(fast !== null && fast.next !== null) {
        prev = slow
        slow = slow.next
        fast = fast.next.next
    }
    prev.next = null
    let first = sortList(head)
    let second = sortList(slow)
    let result = merge(first, second)
    return result
    
};
    
function merge(l1: ListNode, l2: ListNode) {
    let head = null
    if(l1.val > l2.val) {
       head = l2
        l2 = l2.next
    } else {
        head = l1
        l1 = l1.next
    }
    let current = head
    while(l1 && l2) {
        if(l1.val > l2.val) {
            current.next = l2
            current = l2
            l2 = l2.next
        } else {
            current.next = l1
            current = l1
            l1 = l1.next
        }
    }
    if(l1) {
        current.next = l1
    }
    if(l2) {
        current.next = l2
    }
    return head
}