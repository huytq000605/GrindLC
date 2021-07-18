function addRungs(rungs: number[], dist: number): number {
    let currentIdx = -1
    let current = 0
    let result = 0
    while(current !== rungs[rungs.length - 1]) {
        let diff = rungs[currentIdx +  1] - current
        if(diff > dist) {
            current += Math.floor(diff / dist) * dist
            result += Math.floor(diff / dist)
        }
        currentIdx++
        // If we add the existing rungs, decrease it
        if(current === rungs[currentIdx]) result--
        current = rungs[currentIdx]
    }
    return result
}