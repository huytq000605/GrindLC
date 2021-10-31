// Definition for node.
class LLNode {
    val: number
    prev: LLNode | null
    next: LLNode | null
    child: LLNode | null
    constructor(val?: number, prev? : LLNode, next? : LLNode, child? : LLNode) {
        this.val = (val===undefined ? 0 : val);
        this.prev = (prev===undefined ? null : prev);
        this.next = (next===undefined ? null : next);
        this.child = (child===undefined ? null : child);
    }
}


 function flatten(head: LLNode | null): LLNode | null {
    let dfs = (current: LLNode | null, prev: LLNode | null) => {
        if(!current) return prev
        current.prev = prev
        let next = current.next
        if(current.child) {
            current.next = current.child
            current.child = null
            current = dfs(current.next, current)
        }
        current.next = next
        return dfs(next, current)
        
    }
    dfs(head, null)
    return head
};