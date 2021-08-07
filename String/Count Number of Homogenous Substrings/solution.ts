function countHomogenous(s: string): number {
    let result = 0
    let count = 0
    let prev = ""
    for(let i = 0; i < s.length; i++) {
        if(i === 0) {
            count++
            prev = s[i]
            if(i === s.length - 1) {
                result += count*(count+1)/2
            }
            continue
        }
        if(s[i] !== prev) {
            result += (count*(count+1)/2) % (1e9+7)
            result = result % (1e9+7)
            count = 1
            prev = s[i]
        } else {
            count++
        }
        if(i === s.length - 1) {
            result += (count*(count+1)/2) % (1e9+7)
            result = result % (1e9+7)
        }
    }
    return result
};