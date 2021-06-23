function findReplaceString(s: string, indices: number[], sources: string[], targets: string[]): string {
    let replaces = []
    for(let i = 0; i < indices.length; i++) {
        let lengthOfWord = sources[i].length;
        if(s.slice(indices[i], indices[i] + lengthOfWord) === sources[i]) {
            replaces.push([indices[i], indices[i] + lengthOfWord, targets[i]])
        }
    }
    replaces.sort((a,b) => b[0] - a[0]) // We can change from right to left, dont need to pay attention to index
    for(let replace of replaces) {
        s = s.slice(0, replace[0] ) + replace[2] + s.slice(replace[1] )
    }
    return s
};

// change from left to right
function findReplaceString2(s: string, indices: number[], sources: string[], targets: string[]): string {
    let replaces = []
    for(let i = 0; i < indices.length; i++) {
        let lengthOfWord = sources[i].length;
        if(s.slice(indices[i], indices[i] + lengthOfWord) === sources[i]) {
            replaces.push([indices[i], indices[i] + lengthOfWord, targets[i]])
        }
    }
    let prefix = 0
    replaces.sort((a,b) => a[0] - b[0]) // Sort
    for(let replace of replaces) {
        s = s.slice(0, replace[0] + prefix) + replace[2] + s.slice(replace[1] + prefix)
        prefix += replace[2].length - (replace[1] - replace[0])
    }
    return s
};