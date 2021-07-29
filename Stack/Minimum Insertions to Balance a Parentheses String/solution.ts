function minInsertions(s: string): number {
    let stack = []
    let result = 0
    for(let i = 0; i < s.length; i++) {
        if(s[i] === "(") {
            stack.push(i)
        } else {
            if(i === s.length - 1 || s[i + 1] !== ")") {
                result++
            } else {
                i++
            }
            if(stack.length === 0) {
                result++
            } else {
                stack.pop()
            }
        }
    }
    while(stack.length) {
        result += 2
        stack.pop()
    }
    return result
};