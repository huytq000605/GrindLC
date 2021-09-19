function findOriginalArray(changed: number[]): number[] {
    changed.sort((a,b) => a-b)
    let result = []
    let freq = new Map()
    for(let num of changed) {
        freq.set(num, (freq.get(num) || 0) + 1)
    }
    if(freq.has(0)) {
        if(freq.get(0) % 2 === 1) return []
        else {
            for(let i = 0; i < freq.get(0) / 2; i++) result.push(0)
        }
    }
    for(let num of changed) {
        if(freq.get(num) === 0 || num === 0) continue
        if(!freq.has(num*2) || freq.get(num * 2) === 0) return []
        result.push(num)
        freq.set(num, freq.get(num) - 1)
        freq.set(num * 2, (freq.get(num * 2)) - 1)
    }
    return result
}; 