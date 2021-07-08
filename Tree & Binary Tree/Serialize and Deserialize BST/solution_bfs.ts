
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
    if(!root) return ""
    let result = ""
    let queue = [root]
    while(queue.length > 0) {
        let current = queue.shift()
        if(!current) {
            result+= "#,"
            continue
        }
        result += `${current.val},`
        queue.push(current.left)
        queue.push(current.right)
    }
    return result.slice(0, result.length - 1)
};

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
    if(data === "") return null
    let arr = data.split(",")
    let root = new TreeNode(Number(arr[0]))
    let queue: any = [root]
    let index = 1
    while(index < arr.length) {
        let current = queue.shift()
        if(arr[index] !== "#") {
            current.left = new TreeNode(Number(arr[index]))
            queue.push(current.left)
        }
        index++
        if(index === arr.length) {
            return root
        }
        if(arr[index] !== "#") {
            current.right = new TreeNode(Number(arr[index]))
            queue.push(current.right)
        }
        index++
    }
    return root
};


/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */