
// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}



function reverseList(head: ListNode | null): ListNode | null {
    if(head == null) return null
    let prev = null
    while(head != null) {
        let nextLoop = head.next
        head.next = prev
        prev = head;
        head = nextLoop
    }
    return prev
};