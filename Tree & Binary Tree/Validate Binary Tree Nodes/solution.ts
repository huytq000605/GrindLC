class Tree {
    parent
    left
    right
    constructor() {
        this.parent = null
        this.left = null
        this.right = null
    }
}

function validateBinaryTreeNodes(n: number, leftChild: number[], rightChild: number[]): boolean {
    let map = new Map() // Save all node of trees
    
    for(let i = 0; i < n; i++) {
        if(!map.has(i)) map.set(i, new Tree())
        if(leftChild[i] !== -1 && !map.has(leftChild[i])) map.set(leftChild[i], new Tree())
        if(rightChild[i] !== -1 && !map.has(rightChild[i])) map.set(rightChild[i] , new Tree())
        if(leftChild[i] !== -1) {
            map.get(i).left = map.get(leftChild[i])
            if(map.get(leftChild[i]).parent !== null) return false // two parent => not a binary tree
            map.get(leftChild[i]).parent = map.get(i)
        }
        if(rightChild[i] !== -1) {
            map.get(i).right = map.get(rightChild[i])
            if(map.get(rightChild[i]).parent !== null) return false // two parent
            map.get(rightChild[i]).parent = map.get(i)
        }
    }
    let root = null
    for(let i = 0; i < n; i++) { // Find root node
        if(map.get(i).parent === null) {
            root = map.get(i)
            break
        }
    }
    let numOfNodes = 0
    let seen = new Set()
    let dfs = (current) => {
        if(!current) return true
        if(seen.has(current)) return false
        seen.add(current)
        numOfNodes++
        if(!dfs(current.left)) return false 
        if(!dfs(current.right)) return false
        return true
    }
        
    if(!dfs(root)) return false // cicular tree
    if(numOfNodes !== n) return false // Two or more seperate trees
    
    
    return true
};