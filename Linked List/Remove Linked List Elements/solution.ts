// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


 function removeElements(head: ListNode | null, val: number): ListNode | null {
    while(head && head.val === val) {
        head = head.next
    }
    let current = head
    while(current) {
        while(current.next && current.next.val === val) {
            current.next = current.next.next
        }
        current = current.next
    }
    return head
};