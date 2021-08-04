function minMutation(start: string, end: string, bank: string[]): number {
    let graph = new Map()
    for(let a of bank) {
        if(!graph.has(start)) graph.set(start, [])
        if(a !== start && (cmp(a , start) === 1)) {
            graph.get(start).push(a)
        }
        for(let b of bank) {
            if(b === a) continue
            if(cmp(a , b) === 1) {
                if(!graph.has(a)) graph.set(a, [])
                if(!graph.has(b)) graph.set(b, [])
                graph.get(a).push(b)
                graph.get(b).push(a) 
            }
            
        }
    }
    
    let queue: any[] = [[start, 0]]
    let seen = new Set()
    while(queue.length) {
        let [current, move] = queue.shift()
        if(current === end) {
            return move
        }
        if(!graph.has(current)) continue
        for(let connect of graph.get(current)) {
            if(seen.has(connect)) continue
            queue.push([connect, move + 1])
            seen.add(connect)
        }
    }
    
    return -1
};

function cmp(a, b) {
    let result = 0
    for(let i = 0; i < a.length; i++) {
        if(a[i] !== b[i]) result++
    }
    return result
}