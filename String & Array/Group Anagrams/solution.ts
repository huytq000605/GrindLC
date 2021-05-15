function groupAnagrams(strs: string[]): string[][] {
    let map = new Map()
    // Create table to set sorted string as key and index of result as value
    let result = []
    let idxResult = 0;
    for(let i = 0; i < strs.length; i++) {
        let copyArr = strs[i].split(''); // Copy the string and make it array
        let copyString = copyArr.sort().join(''); // Sort the array by lexicographically and join it to string
        if(map.has(copyString)) { // If map has sorted string => just push the original string to result[value]
            result[map.get(copyString)].push(strs[i])
            continue;
        }
        // If map don't have the sorted string, then we add to result, create the key for map
        result[idxResult] = [strs[i]]
        map.set(copyString, idxResult);
        idxResult++
    }
    return result;
};