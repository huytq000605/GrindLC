function minimumDeletions(s: string): number {
    let prefixA = Array(s.length).fill(0)
    let prefixB = Array(s.length).fill(0)
    let totalA = 0
    let totalB = 0
    
    for(let i = 0; i < s.length; i++) {
        if(i === 0) {
            if(s[i] === "a") {
                prefixA[0] = 1
                totalA++
            } else {
                prefixB[0] = 1
                totalB++
            }
        } else {
            if(s[i] === "a") {
                prefixA[i] = prefixA[i-1] + 1
                prefixB[i] = prefixB[i-1]
                totalA++
            } else {
                prefixA[i] = prefixA[i-1]
                prefixB[i] = prefixB[i-1] + 1
                totalB++
            }
        }
    }
    
    let result = Math.min(totalA, totalB)
    
    for(let firstBPosition = 1; firstBPosition < s.length; firstBPosition++) {
        let leftDelete = prefixB[firstBPosition - 1]
        let rightDelete = totalA - prefixA[firstBPosition]
        result = Math.min(result, leftDelete + rightDelete)
    }
    return result
};