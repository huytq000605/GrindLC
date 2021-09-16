function minSwaps(s: string): number {
    let zeros = 0
    let ones = 0
    for(let l of s) {
        if(l === "1") ones++
        else zeros++
    }
    let countDiff = (start) => {
        let result = 0
        for(let i = 0; i  < s.length; i++) {
            if(s[i] !== start) result++
            if(start === "0") start = "1"
            else start = "0"
        }
        return result / 2
    }
    let abs = Math.abs(ones - zeros)
    if(abs > 1) return -1
    if(abs === 0) {
        return Math.min(countDiff("0"), countDiff("1"))
    }
    if(zeros > ones) return countDiff("0")
    return countDiff("1")
};