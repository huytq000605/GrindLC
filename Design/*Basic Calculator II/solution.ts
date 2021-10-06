function calculate(s: string): number {
    let arr = []
    let current = ""
    for(let i = 0; i < s.length; i++) {
        if(s[i] === " ") continue
        if(s[i] === "+" || s[i] === "-" || s[i] === "*" || s[i] === "/") {
            arr.push(Number(current))
            current = ""
            arr.push(s[i])
        } else {
            current += s[i]
        }
    }
    if(current !== "") arr.push(Number(current))
    let stack = []
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] === "+" || arr[i] === "-") continue
        if(arr[i] === "*") {
            let bePushed = stack.pop() * arr[i+1]
            i++
            stack.push(bePushed)
        } else if(arr[i] === "/") {
            let divide = stack.pop()
            let bePushed
            if(divide > 0) bePushed = Math.floor(divide / arr[i+1])
            else bePushed = Math.ceil(divide/ arr[i+1])
            i++
            stack.push(bePushed)
        } else {
            if(i > 0 && arr[i-1] === "-") {
                stack.push(-arr[i])
            } else {
                stack.push(arr[i])
            }
        }
        
    }
    let result = 0
    for(let num of stack) result += num
    return result
};