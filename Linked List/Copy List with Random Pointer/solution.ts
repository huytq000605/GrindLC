
// Definition for LLNode.
class LLNode {
    val: number
    next: LLNode | null
    random: LLNode | null
    constructor(val?: number, next?: LLNode, random?: LLNode) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
        this.random = (random===undefined ? null : random)
    }
}


 function copyRandomList(head: LLNode | null): LLNode | null {
    if(!head) return null
    let newList = new LLNode(head.val)
    let headNewList = newList
    let headOldList = head
    let oldMap = new Map()
    while(newList) {
        if(head.random) {
            if(!oldMap.has(head.random)) {
                oldMap.set(head.random, [])
            }
            oldMap.get(head.random).push(newList)
        }
        head = head.next
        if(head) {
            newList.next = new LLNode(head.val)
        }
        newList = newList.next
    }
    newList = headNewList
    let oldList = headOldList
    
    while(newList) {
        if(oldMap.has(oldList)) {
            for(let list of oldMap.get(oldList)) {
                list.random = newList
            }
        }
        newList = newList.next
        oldList = oldList.next
    }
    return headNewList
};