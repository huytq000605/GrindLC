function maxUniqueSplit(s: string): number {
    return split(s, 0, new Map())
};

function split(s: string, start: number, used: Map<string, boolean>) {
    if(start === s.length) {
        return used.size
    }
    let result = 0
    for(let i = start; i < s.length; i++) {
        let beUsedString = s.slice(start, i + 1)
        if(!used.has(beUsedString)) {
            used.set(beUsedString, true)
            result = Math.max(result, split(s, i + 1, used))
            used.delete(beUsedString)
        }
    }
    return result
}