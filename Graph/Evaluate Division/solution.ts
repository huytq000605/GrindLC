function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    let graphMap = new Map()
    for(let [index, equation] of equations.entries()) {
        if(!graphMap.has(equation[0])) {
            graphMap.set(equation[0], new Map())
        }
        if(!graphMap.has(equation[1])) {
            graphMap.set(equation[1], new Map())
        }
        graphMap.get(equation[0]).set(equation[1], values[index])
        graphMap.get(equation[1]).set(equation[0], 1 / values[index])
    }
    let result = []
    for(let query of queries) {
        if(graphMap.has(query[0]) && graphMap.has(query[1])) {
            let seen = new Map()
            result.push(dfs(query[0], query[1], graphMap, seen))
        } else {
            result.push(-1)
        }
        
    }
    return result
};

function dfs(from: string, to: string, graphMap, seen) {
    if(from === to) {
        return 1
    }
    if(seen.has(from)) {
        return -1
    }
    seen.set(from, true)
    if(graphMap.get(from).has(to)) {
        return graphMap.get(from).get(to)
    }
    for(let [connected, value] of graphMap.get(from).entries()) {
        if(seen.has(connected)) continue;
        let res = dfs(connected, to, graphMap, seen)
        if(res !== -1) return value * res
    }
    return -1
}
