function minimumDeleteSum(s1: string, s2: string): number {
    let map = new Map()
    const result = helper(s1, s2, 0, 0, map)
    return result
};

function deadEndSum(s: string, idx: number): number {
    let sum = 0
    for(let i = idx; i < s.length; i++) {
        sum += s.charCodeAt(i)
    }
    return sum;
}

function helper(s1: string, s2: string, i: number, j: number, map): number {
    const key = `${i}-${j}`
    if(map.has(key)) return map.get(key)
    if(i === s1.length || j === s2.length) {
        if(i === s1.length && j === s2.length) {
            return 0
        }
        if(i === s1.length) {
            map.set(key,deadEndSum(s2, j) )
            return map.get(key)
        } else {
            map.set(key, deadEndSum(s1, i));
            return map.get(key)
        }
    }
    
    if(s1[i] === s2[j]) {
        map.set(key, helper(s1,s2, i+1, j+1, map))
    } else {
        const res1 = helper(s1, s2, i+1, j, map) + s1.charCodeAt(i);
        const res2 = helper(s1, s2, i, j+1, map) + s2.charCodeAt(j);
        const resmin = Math.min(res1, res2);
        map.set(key, resmin);
    }
    return map.get(key);
    
    
}