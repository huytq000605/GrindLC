function longestDupSubstring(s: string): string {
    let min = 1
    let max = s.length
    let result = ""
    
    let check = (length: number) => {
        let BASE = 26 // pool of each character
        let MOD = 2**47 - 1 // Big number
        let map = new Map()
        let hash = 0
        let deleteCost = 1
        for(let i = 0; i < length; i++) {
            let charCode = s.charCodeAt(i) - "a".charCodeAt(0)
            hash = (hash * BASE + charCode) % MOD
            deleteCost *= BASE
            deleteCost %= MOD
        }
        map.set(hash, [])
        map.get(hash).push(0)
        for(let i = 1; i <= s.length - length; i++) { // Can start from s.length - length
            let deleteCharCode = s.charCodeAt(i - 1) - "a".charCodeAt(0)
            let appendCharCode = s.charCodeAt(i - 1 + length) - "a".charCodeAt(0)
            
			// Rolling hash
            hash = hash * BASE
            

			// Delete the first old one
            hash -= (deleteCharCode * deleteCost) % MOD
            hash += MOD
            hash %= MOD
            
			// Append the new one
            hash += appendCharCode
            hash %= MOD
        
            // Avoid collision
			// If hash function is good just use hash set
            if(!map.has(hash)) map.set(hash, [])
            let currentString = s.slice(i, i + length)
            for(let start of map.get(hash)) {
                if(currentString === s.slice(start, start + length)) return i
            }
            map.get(hash).push(i)
        }
        return -1
    }
    
    while(min <= max) {
        let length = min + Math.floor((max - min) / 2)
        let res = check(length)
        if(res === -1) {
            max = length - 1
        } else {
            min = length + 1
            result = s.slice(res, res + length)
        }
    }
    
    return result
};