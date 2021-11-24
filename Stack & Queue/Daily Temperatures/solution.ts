function dailyTemperatures(temperatures: number[]): number[] {
    let stack = []
    let result = Array(temperatures.length).fill(0)
    for(let i = 0; i < temperatures.length; i++) {
        while(stack.length && temperatures[stack[stack.length - 1]] < temperatures[i]) {
            let prevIdx = stack.pop()
            result[prevIdx] = i - prevIdx
        }
        stack.push(i)
    }
    return result
};