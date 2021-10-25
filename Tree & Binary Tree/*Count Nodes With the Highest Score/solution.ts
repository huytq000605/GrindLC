function countHighestScoreNodes(parents: number[]): number {
    
    let childrenMap = new Map()
    
    for(let i = 1; i < parents.length; i++) {
        if(!childrenMap.has(parents[i])) childrenMap.set(parents[i], [])
        childrenMap.get(parents[i]).push(i)
    }
    
    let totalNodes = parents.length
    let subTrees = Array(totalNodes).fill(0).map(() => Array(3).fill(1))
    let dfs = (node) => {
        let nodesOnLeftAndRight = 0
        if(childrenMap.has(node)) {
            let children = childrenMap.get(node)
            for(let i = 0; i < children.length; i++) {
                let numOfNodes = dfs(children[i])
                nodesOnLeftAndRight += numOfNodes
                subTrees[node][i] = numOfNodes
            }
        }
        
        subTrees[node][2] = totalNodes - nodesOnLeftAndRight - 1
        if(subTrees[node][2] === 0) subTrees[node][2] = 1
        return nodesOnLeftAndRight + 1
    }
    
    dfs(0)
    let scores = Array(totalNodes)
    let maxScore = 0
    let result = 0
    for(let i = 0; i < scores.length; i++) {
        scores[i] = subTrees[i][0] * subTrees[i][1] * subTrees[i][2]
        if(scores[i] > maxScore) {
            result = 1
            maxScore = scores[i]
        } else if(scores[i] === maxScore) {
            result++
        }
    }
    return result
};