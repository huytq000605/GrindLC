function peopleIndexes(favoriteCompanies: string[][]): number[] {
    let idx = 0
    let keyMap = new Map() // Create a key value for every companies
    for(let i = 0; i < favoriteCompanies.length; i++) {
        for(let str of favoriteCompanies[i]) {
            if(!keyMap.has(str)) {
                keyMap.set(str, idx++)
            }
        }
    }
    
    let freq = Array(favoriteCompanies.length).fill(0).map(() => Array(idx).fill(0)) // at the moment, idx will be number of companies
    
	// We store each list in a freq array
    for(let i = 0; i < favoriteCompanies.length; ++i) {
        for(let str of favoriteCompanies[i]) {
            freq[i][keyMap.get(str)]++
        }
    }
    
    let result = []
    

	// Since favoriteCompanies.length max == 100 => We can compare a list to 99 others still count as O(1)
    let check = (arr: number[], idx: number) => {
        for(let i = 0; i < freq.length; i++) {
            if(i === idx) continue
            let isChild = true
            for(let j = 0; j < arr.length; j++) {
                if(arr[j] > freq[i][j]) {
                    isChild = false
                    break
                }
            }
            if(isChild) return false
        }
        return true
        
    }
    
    for(let i = 0; i < favoriteCompanies.length; i++) {
        if(check(freq[i], i)) {
            result.push(i)
        }
    }
    
    
    return result
};