function minDeletionSize(strs: string[]): number {
    let finalSorted = Array(strs.length - 1).fill(false) // If string[i] vs string[i+1] has been sorted before
	let result = 0
    for(let i = 0; i < strs[0].length; i++) {
        let sorted = Array(strs.length - 1).fill(false) // Current sort for ith character
        let deleteThis = false
        for(let j = 0; j < strs.length - 1; j++) {
            let current = strs[j]
            let next = strs[j + 1]
            if(!finalSorted[j] && current[i] > next[i]) {
                deleteThis = true
				result++
                break
            }
            if(current[i] < next[i]) {
                sorted[j] = true 
            }
        }
        
        if(!deleteThis) { // If dont delete so update
            for(let j = 0; j < strs.length - 1; j++) {
                finalSorted[j] |= sorted[j]
            }
        }
    }
    return result
};