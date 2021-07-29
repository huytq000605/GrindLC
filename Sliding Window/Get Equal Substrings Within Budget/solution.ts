function equalSubstring(s: string, t: string, maxCost: number): number {
    let cost = maxCost
    let result = 0
    let start = 0
    let arr = []
    for(let i = 0; i < s.length; i++) {
        if(s[i] !== t[i]) {
            let diff = Math.abs(s.charCodeAt(i) - t.charCodeAt(i))
            while(diff > cost && arr.length > 0) {
                cost += arr.shift()
                start++
            }
            if(diff > cost) {
                start++
                continue
            } else {
                cost -= diff
                arr.push(diff)
            }
        } else {
            arr.push(0)
        }
        result = Math.max(result, i - start + 1)
    }
    return result
};