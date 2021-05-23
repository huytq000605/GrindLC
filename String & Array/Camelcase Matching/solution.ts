function camelMatch(queries: string[], pattern: string): boolean[] {
    let result = []
    let patternArray = pattern.split('');
    for(let query of queries) {
        const res = checkPattern(query.split(''), patternArray);
        result.push(res)
    }
    return result
};

function checkPattern(str: string[], pattern: string[]): boolean {
    let j = 0;
    for(let i = 0; i < str.length; i++) {
        if(j < pattern.length && str[i] == pattern[j]) {
            j++
        } else {
            if(str[i].toUpperCase() == str[i]) return false
        }
    }
    if (j === pattern.length) return true
    return false
}