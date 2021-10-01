/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

 function rotateRight(head: ListNode | null, k: number): ListNode | null {
    if(!head) return null
    let length = 0  
    let current = head
    while(current) {
        length++
        current = current.next
    }
    k %= length
    if(k === 0) return head
    let newTail = length - k - 1
    current = head
    while(newTail > 0) {
        current = current.next
        newTail--
    }
    let newHead = current.next
    current.next = null
    current = newHead
    while(current.next) {
        current = current.next
    }
    current.next = head
    return newHead
};