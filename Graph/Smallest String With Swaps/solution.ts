function smallestStringWithSwaps(s: string, pairs: number[][]): string {
    let arr = Array(s.length)
    let graph = new Map()
    for(let pair of pairs) {
        if(!graph.has(pair[0])) graph.set(pair[0], [])
        if(!graph.has(pair[1])) graph.set(pair[1], [])
        if(pair[0] === pair[1]) continue
        graph.get(pair[0]).push(pair[1])
        graph.get(pair[1]).push(pair[0])
    }
    
    let seen = new Map()
    for(let i = 0; i < s.length; i++) {
        if(!graph.has(i)) {
            arr[i] = s[i]
            continue
        }
        let stringArr = []
        let indexArr = []
        dfs(s, i, graph, seen, stringArr, indexArr);
        stringArr.sort()
        indexArr.sort((a,b) => a-b)
        for(let i = 0; i < stringArr.length; i++) {
            arr[indexArr[i]] = stringArr[i]
        }
    }
    return arr.join("")
};

function dfs(s: string, index: number, graph: Map<number, number[]>, seen: Map<number, boolean>, stringArr: string[], indexArr: number[]) {
    if(seen.has(index)) {
        return
    }
    seen.set(index, true)
    stringArr.push(s[index])
    indexArr.push(index)
    for(let connectIndex of graph.get(index)) {
        dfs(s, connectIndex, graph, seen, stringArr, indexArr)
    }
}