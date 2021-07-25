class Tree {
    val: string
    children: Map<string, Tree>
    constructor(val) {
        this.val = val
        this.children = new Map<string, Tree>()
    } 
}

function deleteDuplicateFolder(paths: string[][]): string[][] {
    let root = new Tree("")
    for(let path of paths) {
        let current = root
        for(let str of path) {
            if(!current.children.has(str)) {
                const node = new Tree(str)
                current.children.set(str, node)
            }
            current = current.children.get(str)
        }
    }
    
    let seen = new Map()
    let marks = new Set()
    
    function dfs(node: Tree) {
        let str = ""
        if(node.children.size === 0) {
            return node.val
        }
        for(let child of node.children.values()) {
            str += dfs(child)
        }
        if(seen.has(str)) {
            marks.add(node)
            marks.add(seen.get(str))
        } else {
            seen.set(str, node)
        }
        str += node.val
        return str
    }
    
    
    dfs(root)
    
    let result = []
    
    function buildTree(node: Tree, current: string[]) {
        if(current.length !== 0) {
          result.push([...current])  
        }
        for(let child of node.children.values()) {
            if(marks.has(child)) continue
            current.push(child.val)
            buildTree(child, current)
            current.pop()
        }   
    }
    
    buildTree(root, [])
    return result
};
