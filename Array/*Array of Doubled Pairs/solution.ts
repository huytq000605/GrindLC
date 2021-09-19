function canReorderDoubled(arr: number[]): boolean {
    arr.sort((a,b) => {
        if(a < 0 && b < 0) {
            return b-a
        } else {
            return a-b
        }
    })
    
    let freq = new Map()
    for(let num of arr) {
        freq.set(num, (freq.get(num) || 0) + 1)
    }
    
    if(freq.has(0)) {
        if(freq.get(0) % 2 === 1) return false
    }
    
    for(let num of arr) {
        if(freq.get(num) === 0 || num === 0) continue
        if(!freq.has(num * 2) || freq.get(num * 2) === 0) return false
        freq.set(num, freq.get(num) - 1)
        freq.set(num * 2, freq.get(num * 2) - 1)
    }
    
    return true
};