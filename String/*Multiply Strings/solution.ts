function multiply(num1: string, num2: string): string {
    if(num1 === "0" || num2 === "0") return "0"
    let result = Array(num1.length + num2.length).fill(0)
    for(let i = num1.length - 1; i >= 0; i--) {
        for(let j = num2.length - 1; j >= 0; j--) {
            let first = i + j
            let second = i + j + 1
            let sum = Number(num1[i]) * Number(num2[j]) + result[second]
            result[second] = sum % 10
            result[first] += Math.floor(sum / 10)
        }
    }
    
    let finalResult = ""
    let flag = false
    for(let i = 0; i < result.length; i++) {
        if(result[i] !== 0) flag = true
        if(flag) finalResult += result[i]
    }
    return finalResult
    
};