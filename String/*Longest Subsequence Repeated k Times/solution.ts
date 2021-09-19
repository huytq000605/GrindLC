function longestSubsequenceRepeatedK(s: string, k: number): string {
    let result = ""
    
    let checkFreq = (str) => {
        let freq = 0
        let idx = 0
        for(let i = 0; i < s.length; i++) { 
            if(s[i] === str[idx]) {
                idx++
                if(idx === str.length) {
                    idx = 0
                    freq++
                    if(freq === k) return true
                }
            }
        }
        return false
        
    }
    
    let queue: any = [""]
    while(queue.length) {
        let current = queue.shift()
        for(let ch = "a".charCodeAt(0); ch <= "z".charCodeAt(0); ch++) {
            let append = String.fromCharCode(ch)
            let newString = current + append
            if(checkFreq(newString)) {
                if(newString > result || newString.length > result.length) {
                    result = newString
                }
                queue.push(newString)
            }
        }
    }
    
    return result
    
};