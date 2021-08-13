// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}



//  Do not return anything, modify head in-place instead.
 function reorderList(head: ListNode | null): void {
    let current = head
    let tail = null
    let prevMap = new Map()
    while(current) {
        prevMap.set(current, tail)
        tail = current
        current = current.next
    }
    while(true) {
        if(head.next === tail || head === tail) return
        let nextHead = head.next
        let prevTail = prevMap.get(tail)
        if(nextHead === tail) return
        head.next = tail
        tail.next = nextHead
        prevTail.next = null
        tail = prevTail
        head = nextHead
    }
}; 