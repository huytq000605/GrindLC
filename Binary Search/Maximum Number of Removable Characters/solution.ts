function maximumRemovals(s: string, p: string, removable: number[]): number {
    let min = 0
    let max = removable.length
    while(min < max) {
        let mid = min + Math.ceil((max - min + 1) / 2)
        let j = 0
        let rm = new Set()
        for(let i = 0; i < mid; i++) {
            rm.add(removable[i])
        }
        let valid = false
        for(let i = 0; i < s.length; i++) {
            if(rm.has(i)) continue
            if(s[i] === p[j]) {
                j++
                if(j === p.length) {
                    valid = true
                    break
                }
            }
        }
        if(!valid) {
            max = mid - 1
        } else {
            min = mid
        }
    }
    return min
};