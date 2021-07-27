// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


 function insertionSortList(head: ListNode | null): ListNode | null {
    let start = new ListNode(-5001)
    let tail = start
    while(head) {
        if(head.val >= tail.val) {
            tail.next = head
            tail = head
            head = head.next
            tail.next = null
            continue
        }
        
        let current = start
        while(current.next && current.next.val < head.val) {
            current = current.next
        }
        let next = current.next
        current.next = head
        
        head = head.next
        current.next.next = next
    }
    return start.next
};