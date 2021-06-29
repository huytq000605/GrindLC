
// Definition for Node.
class Node {
    val: number
    left: Node | null
    right: Node | null
    next: Node | null
    constructor(val?: number, left?: Node, right?: Node, next?: Node) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
        this.next = (next===undefined ? null : next)
    }
}


 function connect(root: Node | null): Node | null {
    if(!root) return root
    let queue: any = [[root, 0]]
    while(queue.length) {
        let [currentNode, currentLevel] = queue.shift()
        let [nextNode, nextLevel] = queue[0] || [null, -1]
        if(currentLevel === nextLevel) {
           currentNode.next = nextNode 
        } 
        if(currentNode.left) queue.push([currentNode.left, currentLevel + 1])
        if(currentNode.right) queue.push([currentNode.right, currentLevel + 1])
    }
    return root
};