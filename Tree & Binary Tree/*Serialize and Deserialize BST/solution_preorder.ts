// Definition for a binary tree node.
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}


/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
    let dfs = (current) => {
        if(!current) return "#,"
        let val = `${current.val}`
        let left = dfs(current.left)
        let right = dfs(current.right)
        return `${val},${left}${right}`
    }
    let result = dfs(root)
    return result.slice(0, result.length - 1)
};

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
    let index = 0
    
    if(data === "#") return null
    let val = data.split(",")
 
    
    let dfs = () => {
        if(val[index] === "#") return null
        let current = new TreeNode(Number(val[index]))
        index++
        current.left = dfs()
        index++
        current.right = dfs()
        return current
    }
    let result = dfs()
    return result
};


/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */