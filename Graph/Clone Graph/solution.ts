// Definition for Node.
class GraphNode {
    val: number
    neighbors: GraphNode[]
    constructor(val?: number, neighbors?: GraphNode[]) {
        this.val = (val===undefined ? 0 : val)
        this.neighbors = (neighbors===undefined ? [] : neighbors)
    }
}


 function cloneGraph(node: GraphNode | null): GraphNode | null {
	if(!node) return null
   let map = new Map()  
   let head = node.val
   let dfs = (current) => {
	   map.set(current.val, new GraphNode(current.val))
	   for(let connect of current.neighbors) {
		   if(!map.has(connect.val)) dfs(connect)
	   }
   }
   dfs(node)
   
   let seen = new Set()
   
   dfs = (current) => {
	   seen.add(current.val)
	   for(let connect of current.neighbors) {
		   map.get(current.val).neighbors.push(map.get(connect.val))
		   if(!seen.has(connect.val)) {
			   dfs(connect)
		   }
	   }
   }
   
   dfs(node)
   
   return map.get(head)
};