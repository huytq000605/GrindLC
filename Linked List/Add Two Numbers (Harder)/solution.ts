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
    l1 = reverseLinkedList(l1)
    l2 = reverseLinkedList(l2)
    let head
    let current = null
    let remember = 0
    while(l1 || l2) {
        let num1 = l1 ? l1.val: 0
        let num2 = l2 ? l2.val : 0
        let sum = num1 + num2 + remember
        remember = Math.floor(sum / 10)
        sum = sum % 10
        if(!head) {
            current = new ListNode(sum)
            head = current
        } else {
            current.next = new ListNode(sum)
            current = current.next
        }
        if(l1) l1 = l1.next
        if(l2) l2 = l2.next
    }
    
    if(remember) current.next = new ListNode(remember)
    return reverseLinkedList(head)
    
};

function reverseLinkedList(head) {
    let prev = null;
    while(head) {
        let next = head.next
        head.next = prev
        prev = head
        head = next
    }
    return prev
}