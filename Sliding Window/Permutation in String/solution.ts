function checkInclusion(s1: string, s2: string): boolean {
    let arr = Array(26).fill(0)
    let p = new Set()
    for(let i = 0; i < s1.length; i++) {
        arr[s1.charCodeAt(i) - "a".charCodeAt(0)]++
    }
    function check() {
        for(let i = 0; i < arr.length; i++) {
            if(arr[i] !== 0) return false
        }
        return true
    }
    
    let start = 0
    
    for(let i = 0; i < s1.length && i < s2.length; i++) {
        arr[s2.charCodeAt(i) - "a".charCodeAt(0)]--
    }
    if(check()) {
        return true
    }
    
    for(let i = s1.length; i < s2.length; i++) {
        arr[s2.charCodeAt(start) - "a".charCodeAt(0)]++
        start++
        arr[s2.charCodeAt(i) - "a".charCodeAt(0)]--
        if(check()) {
            return true
        }
    }
    return false
    
};


