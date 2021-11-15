function removeInvalidParentheses(s: string): string[] {
    let queue = []
    queue.push(s)
    let queueNextLevel = []
    let seen = new Set()
    let validThisLevel = []
    while(queue.length) {
        let str = queue.pop()
        if(!seen.has(str)) {
            seen.add(str)
            if(isValid(str)) {
                validThisLevel.push(str)
            }
            for(let i = 0; i < str.length; i++) {
                if(str[i] === "(" || str[i] === ")") {
                    queueNextLevel.push(str.slice(0, i) + str.slice(i + 1))
                }
            }
        }
        
        if(!queue.length) {
            if(validThisLevel.length > 0) {
                return validThisLevel
            } else {
                [queue, queueNextLevel] = [queueNextLevel, queue]
                validThisLevel = []
                seen.clear()
            }
        }
        
    }
    // Never reach here
    return []
};

function isValid(str) {
    let stack = 0
    for(let l of str) {
        if(l === "(") {
            stack++
        } else if(l === ")") {
            if(stack <= 0) return false
            stack--
        }
    }
    return stack === 0
}