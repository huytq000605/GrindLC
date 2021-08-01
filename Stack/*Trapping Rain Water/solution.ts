/*
 *  The idea is each time we meet a height that are >= top of stack
 *  Pop from the stack, it's the bottom will being rain
 *  If we dont have anything in the stack then theres nothing to hold rain => break
 *  If we have at least a height to hold the rain, then we + it to result
 *  We keep doing it again
*/


function trap(height: number[]): number {
    let index = 0
    for(; index < height.length; index++) {
        if(height[index] !== 0) break
    }
    let result = 0
    let stack = [index]
    for(let i = index + 1; i < height.length; i++) {
        while(stack.length && height[i] >= height[stack[stack.length - 1]]) {
            let btm = height[stack.pop()]
            if(!stack.length) {
                break
            }
            let start = stack[stack.length - 1]
            result += (Math.min(height[start], height[i]) - btm) * (i - start - 1)
        }
        stack.push(i)
    }
    return result
};
