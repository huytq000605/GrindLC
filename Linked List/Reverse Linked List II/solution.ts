
// Definition for singly-linked list.

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


 function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    if(left == right) {
        return head;
    }
    let index = 1;
    let result = head;
    let prev = null
    let beforeReverse = null;
    let afterReverse = null;
    let firstReverse = null;
    let lastReverse = null;
    while(head) {
        if(index == left) {
            beforeReverse = prev;
            firstReverse = head;
        }
        if(index == right) {
            lastReverse = head;
            afterReverse = head.next;
            if(beforeReverse) {
                beforeReverse.next = lastReverse
            }
            firstReverse.next = afterReverse
        }
        if(index < left) {
            prev = head;
            head = head.next
            index++
            continue
        }
        if(index > right) {
            break;
        }
        let nextNode = head.next;
        head.next = prev
        prev = head
        head = nextNode;
        index++
    }
    if(left == 1) {
        return lastReverse
    }
    return result
    
};