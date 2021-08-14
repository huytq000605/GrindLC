function findRepeatedDnaSequences(s: string): string[] {
    let map = new Map()
    let result = []
    let current = ""
    for(let i = 0; i < s.length; i++) {
        current += s[i]
        if(current.length > 10) {
            current = current.slice(1)
        }
        if(current.length === 10) {
            if(!map.has(current)) {
                map.set(current, false)
            } else if(map.get(current) === false) {
                map.set(current, true)
                result.push(current)
            }
        }
    }
    return result
};