function maximumGain(s: string, x: number, y: number): number {
    let result = 0
    let stack = []
    let indexUsed = new Set()
    if(x > y) { // Remove all "ab"
        for(let i = 0; i < s.length; i++) {
            if(s[i] === "b") {
                if(stack.length) {
                    result += x
                    indexUsed.add(stack.pop())
                    indexUsed.add(i)
                }
            } else if(s[i] === "a") {
                stack.push(i)
            } else {
                stack = []
            }
        }
    } else if(x < y) { // Remove all "ba"
        for(let i = 0; i < s.length; i++) {
            if(s[i] === "a") {
                if(stack.length) {
                    result += y
                    indexUsed.add(stack.pop())
                    indexUsed.add(i)
                }
                
            } else if(s[i] === "b") {
                stack.push(i)
            } else {
                stack = []
            }
        }
    }
    stack = []
    for(let i = 0; i < s.length; i++) { // + All the remaining
        if(indexUsed.has(i)) continue
        if(s[i] === "a") {
            if(stack.length && stack[stack.length - 1] === "b") {
                result += y
                stack.pop()
            } else {
                stack.push("a")
            }
            continue
        }
        if(s[i] === "b") {
            if(stack.length && stack[stack.length - 1] === "a") {
                result += x
                stack.pop()
            } else {
                stack.push("b")
            }
            continue
        }
        stack = []
    }
    return result
};