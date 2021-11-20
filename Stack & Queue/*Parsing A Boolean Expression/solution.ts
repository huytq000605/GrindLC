function parseBoolExpr(expression: string): boolean {
    let stack = []
    for(let i = 0; i < expression.length; i++) {
        if(expression[i] === "(") {
            stack.push(i)
        } else if(expression[i] === ")") {
            let start = stack.pop()
            let operator = expression[start - 1]
            let replace = ""
            if(operator === "!") {
                if(expression[start + 1] === "f") replace = "t"
                else replace = "f"
                
            } else if(operator === "&") {
                replace = "t"
                for(let j = start + 1; j < i; j++) if(expression[j] === "f") replace = "f"
            } else {
                replace = "f"
                for(let j = start + 1; j < i; j++) if(expression[j] === "t") replace = "t" 
            }
            expression = expression.slice(0, start - 1) + replace + expression.slice(i + 1)
            i = start - 1
        }
    }
    return expression === "t"
};