// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


function partition(head: ListNode | null, x: number): ListNode | null {
    let less = new ListNode(-1)
    let greaterOrEqual = new ListNode(-1)
    let h1 = less 
    let h2 = greaterOrEqual 
    
    while(head) {
        if(head.val < x) {
            less.next = head
            less = less.next
        } else {
            greaterOrEqual.next = head
            greaterOrEqual = greaterOrEqual.next
        }
        head = head.next
    }
    
    less.next = h2.next
    greaterOrEqual.next = null
    return h1.next
};