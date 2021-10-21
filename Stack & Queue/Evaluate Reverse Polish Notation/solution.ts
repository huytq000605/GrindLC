function evalRPN(tokens: string[]): number {
    let stack = []
    for(let token of tokens) {
        if(token === "+" || token === "-" || token === "*" || token === "/") {
            let num2 = stack.pop()
            let num1 = stack.pop()
            switch(token) {
                case "+": 
                    stack.push(num1 + num2)
                    break
                case "-":
                    stack.push(num1 - num2)
                    break
                case "*":
                    stack.push(num1 * num2)
                    break
                case "/":
                    if(num1 * num2 < 0) {
                        stack.push(Math.ceil(num1 / num2))
                    } else {
                        stack.push(Math.floor(num1 / num2))
                    }
                    
                    break
            }
            
        } else {
			stack.push(Number(token)) 
        }
        
    }
    return stack[0]
};