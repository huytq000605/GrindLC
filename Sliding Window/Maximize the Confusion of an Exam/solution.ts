function maxConsecutiveAnswers(ans: string, k: number): number {
    let start = 0
    let result = 0
    let originalK = k
    
    for(let i = 0; i < ans.length; i++) {
        if(ans[i] === "F") {
            k--
            while(k < 0) {
                if(ans[start] === "F") k++
                start++
            }
        }
        result = Math.max(result, i - start + 1)
    }
    
    k = originalK
    start = 0
    
    for(let i = 0; i < ans.length; i++) {
        if(ans[i] === "T") {
            k--
            while(k < 0) {
                if(ans[start] === "T") k++
                start++
            }
        }
        result = Math.max(result, i - start + 1)
    }
    return result
};