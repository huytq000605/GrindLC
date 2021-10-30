function braceExpansionII(expression: string): string[] {
    let result = []
    
    let dfs = (idx: number, current: string, stack: number[]) => {
        let originalCurrent = current
        for(let i = idx; i < current.length; i++) {
            if(current[i] === "{") {
                stack.push(i)
            } else if(current[i] === "}") {
                let start = stack.pop()
                let selections = current.slice(start + 1, i).split(",")
                for(let selection of selections) {
                    current = current.slice(0, start) + selection + current.slice(i + 1)
                    dfs(start + selection.length, current, [...stack])
                    current = originalCurrent
                }
                return
            }
        }
        result.push(current)
    }
    
    dfs(0, expression, [])
    let finalResult = []
    for(let res of result) {
        finalResult.push(...res.split(","))
    }
    return Array.from(new Set(finalResult)).sort()
    
};