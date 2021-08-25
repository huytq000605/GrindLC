// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


 function deleteDuplicates(head: ListNode | null): ListNode | null {
    if(!head) return null
    let getThis = true
    let first = head
    head = head.next
    while(head) {
        if(head.val === first.val) {
            getThis = false
            head = head.next
        } else {
            break
        }
    }
    if(getThis) {
        first.next = deleteDuplicates(first.next)
        return first
    } else {
        return deleteDuplicates(head)
    }
    
};