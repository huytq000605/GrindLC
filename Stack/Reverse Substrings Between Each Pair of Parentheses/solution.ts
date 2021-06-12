function reverseParentheses(s: string): string {
    let stack = []
    let result = s
    for(let i = 0; i < result.length; i++) {
        if(result[i] == "(") {
            stack.push(i)
            continue;
        }
        if(result[i] == ")") {
            let start = stack.pop()
            result = result.slice(0, start) + reverse(result.slice(start+1, i)) + result.slice(i + 1) // Leave the ( and )
            i-=2 // Because we remove ( and )
            continue;
        }
    }
    return result
};

function reverse(s: string): string {
    let result = ""
    for(let i = s.length - 1; i >= 0; i--) {
        result += s[i]
    }
    return result
}