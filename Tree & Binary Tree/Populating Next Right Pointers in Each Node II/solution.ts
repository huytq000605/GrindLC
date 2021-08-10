/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     left: Node | null
 *     right: Node | null
 *     next: Node | null
 *     constructor(val?: number, left?: Node, right?: Node, next?: Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

 function connect(root: Node | null): Node | null {
    if(!root) return null
    let queue: any = [[root, 0]]
    while(queue.length) {
        let [currentNode, currentLevel] = queue.shift()
        let left = currentNode.left
        let right = currentNode.right
        if(queue.length && queue[0][1] === currentLevel) {
            currentNode.next = queue[0][0]
        }
        if(left) queue.push([left, currentLevel + 1])
        if(right) queue.push([right, currentLevel + 1])
    }
    
    return root
};