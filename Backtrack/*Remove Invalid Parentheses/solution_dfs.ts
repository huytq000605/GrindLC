function removeInvalidParentheses(s: string): string[] {
    let stack = []
    let notValidOpen = 0
    let notValidClose = 0
    for(let l of s) {
        if(l === "(") {
            stack.push(l)
        } else if(l === ")") {
            if(!stack.length) notValidClose++
            else stack.pop()
        }
    }
    notValidOpen = stack.length
    let result = new Set()
    let dfs = (idx, discardOpen, discardClose, stack, currentString) => {
        if(discardOpen < 0 || discardClose < 0) return
        if(idx >= s.length) {
            if(discardOpen === 0 && discardClose === 0 && stack === 0) result.add(currentString)
            return
        }
        
        if(s[idx] === "(") {
            dfs(idx + 1, discardOpen, discardClose, stack + 1, currentString + "(")
            dfs(idx + 1, discardOpen - 1, discardClose, stack, currentString)
        } else if(s[idx] === ")") {
            dfs(idx + 1, discardOpen, discardClose - 1, stack, currentString)
            if(stack > 0) {
                dfs(idx + 1, discardOpen, discardClose, stack - 1, currentString + ")")
            } 
        } else {
            dfs(idx + 1, discardOpen, discardClose, stack, currentString + s[idx])
        }
    }
    
    dfs(0, notValidOpen, notValidClose, 0, "")
    return Array.from(result) as string[]
};