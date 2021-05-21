/*
Input: a random string with only abc
and a random map like map = {
        'a': 2, 'b': 3, 'c':4
    }
Output: A shortest substring that contains at least 2 'a', 3 'b' and 4 'c' 
Idea: Sliding window
*/

function getShortestSubstring(str: string, map: Map<string, number>) {
    let start = 0;
    let result = Number.MAX_SAFE_INTEGER;
    for(let end = 0; end < str.length; end++) {
        if(map.has(str[end])) map.set(str[end], map.get(str[end]) - 1);
        while(isMapFullfilled(map) === true) {
            result = Math.min(result, end - start + 1);
            if(map.has(str[start])) map.set(str[start], map.get(str[start]) + 1);
            start++;
        }
    }
}

function isMapFullfilled(map: Map<string,number>): boolean {
    for(const [alphabet, required] of map.entries()) {
        if(required > 0) return false;
    }
    return true;
}