class LLNode {
    next: LLNode
    val: number
    constructor(val: number) {
        this.val = val
    }
}

function getWinner(arr: number[], k: number): number {
    let winner: number
    let winCount = 0
    let prev = null
    let head: LLNode
    for(let num of arr) {
        let curr = new LLNode(num)
        if(prev) {
            prev.next = curr
        } else {
            head = curr
        }
        prev = curr
    }
    let tail = prev
    while(true) {
        let next = head.next
        if(next.val > head.val) {
            [next.val, head.val] = [head.val, next.val]
        }
        head.next = next.next
        next.next = null
        tail.next = next
        tail = next
        if(winner === head.val) {
            winCount++
        } else {
            winner = head.val
            winCount = 1
        }
        if(winCount === k) {
            return winner
        }
        
    }
    return 0
};