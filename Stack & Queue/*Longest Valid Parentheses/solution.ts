function longestValidParentheses(s: string): number {
    let stack = []
    let result = 0
    let longest = Array(s.length).fill(0)
    for(let i = 0; i < s.length; i++) {
        if(s[i] === "(") {
            stack.push(i)
        } else {
            if(stack.length) {
                let start = stack.pop()
                let prev = 0
                if(start - 1 >= 0) {
                    prev = longest[start - 1]
                }
                result = Math.max(result, i - start + 1 + prev)
                longest[i] = i - start + 1 + prev
            }
        }
    }
    return result
};