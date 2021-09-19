function scoreOfParentheses(s: string): number {
    let open = 0
    let result = 0
    for(let i = 0; i < s.length; i++) {
        if(s[i] === "(") {
            open++
            if(s[i+1] === ")") {
                result += 1 << (open - 1)
            }
        }
        if(s[i] === ")") {
            open--
        }
    }
    return result
}
