function convert(s: string, numRows: number): string {
    let row = Array(numRows).fill("")
    let i = 0
    while(i < s.length) {
        for(let j = 0; j < numRows && i < s.length; i++, j++) {
            row[j] += s[i]
        }
        for(let j = numRows - 2; j >= 1 && i < s.length; j--, i++) {
            row[j] += s[i]
        }
    }
    
    let result = ""
    for(let r of row) {
        result += r
    }
    return result
};