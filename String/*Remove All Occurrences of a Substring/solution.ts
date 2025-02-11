function removeOccurrences(s: string, part: string): string {
    let stack = []
    let check = () => {
        let i = stack.length - 1
        let j = part.length - 1
        while(i >= 0 && j >= 0 && stack[i] === part[j]) {
            i--
            j--
        }
        return j === -1
    }
    
    for(let i = 0; i < s.length; i++) {
        stack.push(s[i])
        while(stack.length >= part.length && check()) {
            for(let i = 0; i < part.length; i++) stack.pop()
        }
    }
    return stack.join("")
};