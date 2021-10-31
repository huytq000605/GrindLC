// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


 function nodesBetweenCriticalPoints(head: ListNode | null): number[] {
    let min = Number.MAX_SAFE_INTEGER
    let firstIdx = -1
    let lastIdx = 0
    let idx = 0
    
    let prev = head
    head = head.next
    while(head.next) {
        let next = head.next
        if((head.val < prev.val && head.val < next.val) || (head.val > prev.val && head.val > next.val)) {
            if(firstIdx === -1) {
                firstIdx = idx
                lastIdx = idx
            } else {
                min = Math.min(min, idx - lastIdx)
                lastIdx = idx
            }
        }
        
        idx++
        prev = head
        head = next
    }
    if(firstIdx === -1 || lastIdx === firstIdx) return [-1, -1]
    return [min, lastIdx - firstIdx]

};