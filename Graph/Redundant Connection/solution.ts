/*
Think this graph, each node will have only max of 2 connected node to it => dfs function just need to save the previous Node it went
We continue dfs the next node to find target
*/

class GraphNode {
    val: number
    connected: GraphNode[]
    
    constructor(val) {
        this.val = val
        this.connected = []
    }
}

function dfs(current: GraphNode, target: GraphNode, preVisit: GraphNode) {
    if(!current) {
        return false
    }
    if(current === target) {
        return true
    }
    for(let connect of current.connected) {
        if(preVisit !== connect) {
            if(dfs(connect, target, current)) {
                return true
            }
        }
    }
    return false
    
}
function findRedundantConnection(edges: number[][]): number[] {
    let mapGraphNode = new Map()
    let result: number[]
    for(let edge of edges){
        if(!mapGraphNode.has(edge[0])) {
            mapGraphNode.set(edge[0], new GraphNode(edge[0]))
        }
        if(!mapGraphNode.has(edge[1])) {
            mapGraphNode.set(edge[1], new GraphNode(edge[1]))
        }
        const u = mapGraphNode.get(edge[0])
        const v = mapGraphNode.get(edge[1])
        if(dfs(u, v, null)) {
            result = edge
        } else {
            u.connected.push(v)
            v.connected.push(u)
        }
    } 
    return result
};