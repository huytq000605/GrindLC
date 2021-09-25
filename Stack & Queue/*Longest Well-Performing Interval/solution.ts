function longestWPI(hours: number[]): number {
    let days = hours.map((e) => {
        if(e > 8) return 1
        else return -1
    })
    
    let prefix = Array(hours.length)
    prefix[0] = days[0]
    for(let i = 1; i < prefix.length; i++) {
        prefix[i] = prefix[i-1] + days[i]
    }
    let stack = []
    for(let i = 0; i < prefix.length; i++) {
        if(!stack.length || prefix[i] < prefix[stack[stack.length - 1]]) {
            stack.push(i)
        }
    }
    let result = 0
    
    for(let i = prefix.length -1; i >= 0; i--) {
        if(prefix[i] > 0) {
            result = Math.max(result, i + 1)
        }
        while(stack.length && prefix[i] > prefix[stack[stack.length - 1]]) {
            result = Math.max(result, i - stack.pop())
        }
    }
    return result
};