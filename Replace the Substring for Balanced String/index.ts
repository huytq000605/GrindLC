function balancedString(s: string): number {
    let map = new Map()
    let map2 = new Map()
    let result = Number.MAX_SAFE_INTEGER

    // Get all frequency of each word in string
    for(let i = 0; i < s.length; i++) {
        map.set(s[i], (map.get(s[i]) || 0) + 1);
    }
    
    for(let [key,value] of map.entries()) {
        if(value > s.length/4) {
            map2.set(key, value - s.length/4);
        }
    }
    if(map2.size === 0) return 0;
    /* Must find a minimum length of substring that contains at least [key] value times of map2;
    I have a map like map = {
        'a': 2, 'b': 3, 'c':4
    }
    and a random string so the result after this i get is a substring that contains at least 2 'a', 3 'b' and 4 'c' having minimum length
    */
    let start = 0;
    for(let i = 0; i < s.length; i++) {
        if(map2.has(s[i])) map2.set(s[i], map2.get(s[i]) -1);
        while(helper(map2)) {
            result = Math.min(result, i - start + 1);
            if(map2.has(s[start])) map2.set(s[start], map2.get(s[start]) +1);
            start++
        }
    }
    return result
};

function helper(map) {
    for(let [key,value] of map.entries()) {
        if(value > 0) return false;
    }
    return true;
}