function kthGrammar(n: number, k: number): number {
    let result
    if(n === 1) {
        result = "0"
    } else if(n === 2) {
        result = "01"
    } else if(n === 3) {
        result = "0110"
    } else {
        let currentLength = Math.pow(2, n - 1)
        if(k > currentLength / 2) {
            return 1 - kthGrammar(n - 1, k - currentLength / 2)
        } else {
            return kthGrammar(n - 1, k)
        }
    }
    return result[k-1]
};