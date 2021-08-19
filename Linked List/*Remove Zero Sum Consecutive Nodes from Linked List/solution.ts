// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


 function removeZeroSumSublists(head: ListNode | null): ListNode | null {
    let stack = []
    let prefixSum = []
    let map = new Map()
    map.set(0, -1)
    while(head) {
        if(head.val === 0) { // Ignore zero value
            head = head.next
            continue
        }
        if(!stack.length) { // Empty stack && prefixSum
            stack.push(head)
            prefixSum.push(head.val)
            map.set(head.val, 0)
        } else {
            let currentPrefix = prefixSum[prefixSum.length - 1] + head.val
            stack.push(head)
            prefixSum.push(currentPrefix)
            if(map.has(currentPrefix)) {
                for(let i = stack.length - 1; i > map.get(currentPrefix); i--) { // Delete from index of currentPrefix that already in hashmap + 1 to end
                    const deletePrefix = prefixSum.pop()
                    stack.pop()
                    // Delete all key in the range
                    // Remember to not delete the currentPrefix key because it will be the last element after delete
                    if(deletePrefix !== currentPrefix) {
                        map.delete(deletePrefix)
                    }
                }
            } else {
                map.set(currentPrefix, stack.length - 1)
            }
        }
        head = head.next
    }
    
    //Build the linked list from remaining nodes
    if(!stack.length) return null
    head = stack[0]
    for(let i = 0; i < stack.length; i++) {
        if(i === stack.length - 1) {
            stack[i].next = null
            break }
        stack[i].next = stack[i + 1]
    }
    return head
    
};