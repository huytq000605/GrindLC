
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


function countPairs(root: TreeNode | null, distance: number): number {
	// build Parent map
    let parentMap = new Map()
    buildParentMap(root, parentMap)
	// Get all leaf nodes of this tree
    let leafNodes = getLeafNode(root)
    let result = 0;
    for(let leafNode of leafNodes) {
        let seen = new Map()
        result += dfs(leafNode, distance, seen, parentMap, true)
    }
    return result / 2
    
};

function buildParentMap(node: TreeNode | null, parentMap: Map<TreeNode, TreeNode>) {
    if(node.left) {
        parentMap.set(node.left, node)
        buildParentMap(node.left, parentMap)
    }
    if(node.right) {
        parentMap.set(node.right, node)
        buildParentMap(node.right, parentMap)
    }
}

function getLeafNode(node: TreeNode, result: TreeNode[] = []): TreeNode[] {
    if(!node) {
        return result
    }
    if(!node.left && !node.right) {
        result.push(node)
        return result
    } else {
        getLeafNode(node.left, result)
        getLeafNode(node.right, result)
        return result
    }
    
}

function dfs(node: TreeNode, distance: number, seen: Map<TreeNode, boolean>, parentMap: Map<TreeNode, TreeNode>, starting = false) {
    if(distance < 0) {
        return 0
    }
    if(!node) {
        return 0
    }
    if(seen.has(node)) {
        return 0
    }
    seen.set(node, true)
    if(!node.left && !node.right && !starting) {
        return 1
    }
    return dfs(node.left, distance - 1, seen, parentMap) + dfs(node.right, distance - 1, seen, parentMap) + dfs(parentMap.get(node), distance - 1, seen, parentMap)
    
}