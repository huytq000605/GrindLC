function calculate(s: string): number {
    let stack = []
    for(let i = 0; i < s.length; i++) {
        if(s[i] === "(") {
            stack.push(i)
        } else if(s[i] === ")") {
            let open = stack.pop()
            s = s.slice(0, open) + calculateNoBracket(s.slice(open + 1, i)) + s.slice(i + 1)
            i = open - 1
        }
    }
    return calculateNoBracket(s)
};

function calculateNoBracket(s: string): number {
    let arr = []
    let negative = false
    let current = ""
    for(let i = 0; i < s.length; i++) {
        if(s[i] === " ") continue
        if(s[i] === "+" || s[i] === "-" || s[i] === "*" || s[i] === "/") {
            if(current === "" && s[i] === "-") {
                negative = true
                continue
            }
            if(negative) {
                arr.push(-Number(current))
                negative = false
            } else {
                arr.push(Number(current))
            }
            arr.push(s[i])
            current = ""
        } else {
            current += s[i]
        }
    }
    if(negative) {
        arr.push(-Number(current))
    } else {
        arr.push(Number(current))
    }
    let remaining = []
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] === "+" || arr[i] === "-") continue
        if(arr[i] === "*") {
            let pop = remaining.pop()
            let result = arr[i+1] * pop
            i++
            remaining.push(result)
        } else if(arr[i] === "/") {
            let pop = remaining.pop()
            let swap = false
            if(pop < 0) {
                swap = true
                pop = -pop
            }
            let result = Math.floor(pop / arr[i+1])
            i++
            if(swap) result = -result
            remaining.push(result)
        } else {
            if(arr[i-1] === "-") remaining.push(-arr[i])
            else remaining.push(arr[i])
            negative = false
        }
    }
    let result = 0
    for(let num of remaining) {
        result += num
    }
    return result
};