function maxRepOpt1(text: string): number {
	// Group repeated letters into group
	// For each group, we just save the interval (starting index and ending index)
    let map = new Map()
    let result = 0
    for(let i = 0; i < text.length; i++) {
        if(!map.has(text[i])) map.set(text[i], [])
        let arr = map.get(text[i])
        if(arr.length) {
            if(arr[arr.length -1][1] === i - 1) {
                arr[arr.length - 1][1] = i
            } else {
                arr.push([i, i])
            }
        } else {
            arr.push([i, i])
        }
    }
	// Choosing starting letter for substring
    for(let startingLetter of map.keys()) {
        let arr = map.get(startingLetter)
		// If has only 1 group, then just count the maximum substring it has
        if(arr.length === 1) {
            result = Math.max(result, arr[0][1] - arr[0][0] + 1)
        }
		// If has 2 groups, the way we can get the longest substring can be concat two groups (if can) or get maximum of length of each group + 1 (getting 1 from the remaining group)
        if(arr.length === 2) {
            if(arr[1][0] - arr[0][1] === 2) {
                result = Math.max(result, arr[1][1] - arr[0][0])
            } else {
                result = Math.max(result, arr[0][1] - arr[0][0] + 1 + 1, arr[1][1] - arr[1][0] + 1 + 1)
            }
        }
		// The difference between 2 groups, and > 2 groups is that, when concat 2 groups, if we have only 2 groups, we must use the letter from these 2 groups to concating them, but when we have > 2 groups, we can get the letter to concat in another groups
		// If it has >2 groups, then we can get the result by concat two groups by using 1 letter not from these 2 groups, if we cant concat then we try to use that group's length + 1 (swapping from another group)
        if(arr.length > 2) {
            for(let index = 0; index < arr.length - 1; index++) {
                if(arr[index+1][0] - arr[index][1] === 2) {
                    result = Math.max(result, arr[index + 1][1] - arr[index][0] + 1)
                } else {
                    result = Math.max(result, arr[index][1] - arr[index][0] + 1 + 1)
                }
            }
			// We must check for the length of the last group too
            result = Math.max(result, arr[arr.length - 1][1] - arr[arr.length - 1][0] + 1 + 1)
        }
        
    }
    return result
};