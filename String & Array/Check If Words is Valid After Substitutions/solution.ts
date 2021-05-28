// Straight foward
function isValid(s: string): boolean {
    let stack = []
    for(let i = 0; i < s.length; i++) {
        stack.push(s[i]);
        let check = stack.slice(-3).join('')
        if(check === 'abc') {
            stack = stack.slice(0,-3)
        }
    }
    if(stack.length === 0) return true;
    return false;
};

// More optimize

function isValid2(s: string): boolean {
    let stack = []
    for(let i = 0; i < s.length; i++) {
        stack.push(s[i])
        while(stack[stack.length - 1] == 'c') {
            stack.pop()
            if(stack.pop() !== 'b') return false
            if(stack.pop() !== 'a') return false;
        }
    }
    return stack.length == 0
}