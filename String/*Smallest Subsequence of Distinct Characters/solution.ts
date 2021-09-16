function smallestSubsequence(s: string): string {
    let lastIndex = new Map()
    let seen = new Map()
    let stack = ""
    for(let i = 0; i < s.length; i++) {
        lastIndex.set(s[i], i);
    }
    for(let i = 0; i < s.length; i++) {
        if(seen.has(s[i])) {
            continue;
        }
        
        while(stack.length > 0) {
            const last = stack.length - 1;
            if(stack[last] > s[i] && lastIndex.get(stack[last]) > i) {
                seen.delete(stack[last])
                stack = stack.slice(0, -1)
            } else {
                break
            }
        }
        seen.set(s[i], true)
        stack += s[i]
    }
    return stack
};