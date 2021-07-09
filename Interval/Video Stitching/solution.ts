function videoStitching(clips: number[][], time: number): number {
    clips.sort((a,b) => a[0] - b[0] || a[1] - b[1])
    let cache= new Map()
    let result = helper(clips, 0, Number.MAX_SAFE_INTEGER, Number.MIN_SAFE_INTEGER, time, cache)
    if(result < 0) return -1
    return result
};

function helper(clips: number[][], index: number, start: number, end: number, time: number, cache: Map<string, number>) {
    if(start === 0 && end >= time) { // If current partition fit condition
        return 0
    }
    const key = `${index}-${start}-${end}`
    if(cache.has(key)) {
        return cache.get(key)
    }
    if(index === clips.length) return Number.MIN_SAFE_INTEGER // Out of range
    if(clips[index][0] !== 0 && start !== 0) return Number.MIN_SAFE_INTEGER // No partition that have start = 0 (just to optimize speed)
    if(clips[index][0] > end && end !== Number.MIN_SAFE_INTEGER) return Number.MIN_SAFE_INTEGER // Because we sorted the intervals, so if start of this interval > current end so we cannot combine any interval from this into current
    let getThis = 1 + helper(clips, index + 1, Math.min(start, clips[index][0]), Math.max(end, clips[index][1]), time, cache) // Combine this interval to current
    let passThis = helper(clips, index + 1, start, end, time, cache) // Pass current interval
    if(getThis < 0) {
        cache.set(key, passThis)
        return passThis
    }
    if(passThis < 0) {
        cache.set(key, getThis)
        return getThis
    } 
    cache.set(key, Math.min(getThis, passThis))
    return cache.get(key)
    
    
}