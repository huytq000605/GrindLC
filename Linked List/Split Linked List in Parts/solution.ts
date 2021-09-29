// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


function splitListToParts(head: ListNode | null, k: number): any {
    let len = 0
    let current = head
    while(current) {
        len++
        current = current.next
    }
    let each = Math.floor(len / k)
    let firstN = len - each * k // First N element will have + 1 Linked List node
    let result = Array(k)
    for(let i = 0; i < k; i++) {
        let numOfNode = each
        if(i + 1 <= firstN) numOfNode++
        if(numOfNode === 0) result[i] = null
        for(let j = 0; j < numOfNode; j++) {
            if(j === 0) {
                result[i] = head
            }
            if(j === numOfNode - 1) {
                let next = head.next
                head.next = null
                head = next
                continue
            }
            head = head.next
        }
    }
    return result
};