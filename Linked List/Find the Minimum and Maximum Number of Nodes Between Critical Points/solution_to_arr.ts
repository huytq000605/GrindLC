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
    let arr = []
    while(head) {
        arr.push(head.val)
        head = head.next
    }
    let criticals = []
    let min = Number.MAX_SAFE_INTEGER
    for(let i = 1; i < arr.length; i++) {
        if(arr[i-1] < arr[i] && arr[i] > arr[i+1]) {
            criticals.push(i)
        } else if(arr[i-1] > arr[i] && arr[i] < arr[i+1]) {
            criticals.push(i)        
        }
        
    }
    if(criticals.length < 2) {
        return [-1, -1]
    }
    for(let i = 1; i < criticals.length; i++) {
        min = Math.min(min, criticals[i] - criticals[i - 1])
    }
    return [min, criticals[criticals.length - 1] - criticals[0]]
};