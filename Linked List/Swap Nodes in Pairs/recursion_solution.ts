
// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


 function swapPairs(head: ListNode | null, prev: ListNode | null = null): ListNode | null {
    if(!head) return null;
    const first = head;
    const second = first.next;
    if(second) {
        if(prev)
        prev.next = second;
        const third = second.next;
        first.next = third;
        second.next = first;
        if(third)
        swapPairs(third, first);
        return second;
    }
    return first


};