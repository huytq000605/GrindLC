function groupAnagrams(strs: string[]): string[][] {
    let map = new Map()
    let result = []
    let idxResult = 0;
    for(let i = 0; i < strs.length; i++) {
        let copyArr = strs[i].split('');
        let copyString = copyArr.sort().join('');
        if(map.has(copyString)) {
            result[map.get(copyString)].push(strs[i])
            continue;
        }
        result[idxResult] = [strs[i]]
        map.set(copyString, idxResult);
        idxResult++
    }
    return result;
};
