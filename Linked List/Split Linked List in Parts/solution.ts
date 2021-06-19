
// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


 function splitListToParts(head: ListNode | null, k: number): Array<ListNode | null> {
    let listLength = 0;
    let originalHeadNode = head;
    while(head) {
        listLength++
        head = head.next
    } // Find length of the Linked list

    let minEachPart = Math.floor(listLength / k) // num of min nodes each part have
    let numOfPlusPart = listLength % k // number of starting parts which have minEachPart + 1 nodes
    let result = []

    let current = originalHeadNode;
    for(let i = 1; i <= k; i++) {
        let headNode = current // headNode of this part
        if (!headNode) { // null part
            result.push(null);
            continue;
        }
        if(i <= numOfPlusPart) { // if this part have minEachPart + 1 nodes
            for(let j = 0; j < minEachPart + 1; j++) { // find last node of this part to set next to null
                if(j == minEachPart) {
                    let next = current.next
                    current.next = null
                    current = next;
                } else {
                    current = current.next
                }
            }
        } else { // if this part hafve minEachPart nodes
            for(let j = 0; j < minEachPart; i++) { // find last node of this part to set next to null
                if(i == minEachPart - 1) {
                    let next = current.next
                    current.next = null
                    current = next
                } else {
                    current = current.next
                }
            }
        }
        result.push(headNode)
    }
    return result
};