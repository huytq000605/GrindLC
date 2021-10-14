function isAdditiveNumber(num: string): boolean {
    if(num.length < 3) return false
    let allZero = true
    for(let digit of num) {
        if(digit !== "0") {
            allZero = false
            break
        }
    }
    if(allZero) return true
    let dfs = (idx, prev1, prev2) => {
        if(idx >= num.length) return true
        if(num[idx] === "0") return false
        let sum = `${prev1 + prev2}`
        let len = sum.length
        if(num.slice(idx, idx + len) === sum) {
            if(dfs(idx + len, Number(sum), prev1)) return true
        }
        return false
    }
    for(let i = 1; i <= num.length - 2; i++) {
        if(num[0] === "0" && i > 1) break
        let prev2 = Number(num.slice(0, i))
        for(let j = i + 1; j <= num.length - 1; j++) {
            if(num[i] === "0" && j > i + 1) break
            let prev1 = Number(num.slice(i, j))
            if(dfs(j, prev1, prev2)) return true
        }
    }
    return false

};