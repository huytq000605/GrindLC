function sumOfDistancesInTree(n: number, edges: number[][]): number[] {
    let tree = new Map()
    for(let edge of edges) {
        if(!tree.has(edge[0])) {
            tree.set(edge[0], [])
        }
        if(!tree.has(edge[1])) {
            tree.set(edge[1], [])
        }
        tree.get(edge[0]).push(edge[1])
        tree.get(edge[1]).push(edge[0])
    }
    
    let childCountMap = new Map()

    let result = new Map()
    result.set(0, 0) // 0 is always root of the tree
    
    let dfs = (current: number, distance: number, previous: number) => { // Create childCountMap and set result value for root
        childCountMap.set(current, 0)
        result.set(0, result.get(0) + distance)
        if(tree.has(current)) {
            for(let child of tree.get(current)) {
                if(child === previous) continue // Skip the parent
                childCountMap.set(current, childCountMap.get(current) + dfs(child, distance + 1, current) + 1)
            }
        }
        
        return childCountMap.get(current)
    }
    dfs(0, 0, -1)
    

    let dfs2 = (current: number, previous: number) => { // We always can calculate the result for child node if we know its parent's result
        if(tree.has(current)) {
            for(let child of tree.get(current)) {
                if(child === previous) continue // Skip the parent
				// For each child, we have to consider children of current, children of parent, parent of parent (explaination in assets)
                let res = result.get(current) - childCountMap.get(child) + (childCountMap.get(current) - childCountMap.get(child) - 1) + (n - (childCountMap.get(current) + 1))
                result.set(child, res)
                dfs2(child, current)
            } 
        }
        
    }
    dfs2(0, -1)

    let finalResult = Array(n)
    for(let [key, value] of result.entries()) {
        finalResult[key] = value
    }
    return finalResult
};