function decodeString(s: string): string {
    let result = ""
    let dfs = (idx: number, str: string, stack: number[]) => {
        for(let i = idx; i < str.length; i++) {
            if(str[i] === "[") {
                stack.push(i)   
            } else if(str[i] === "]") {
                let open = stack.pop()
                let startNumber = 0
                for(let i = open - 1; i >= 0; i--) {
                    if(str[i] >= "0" && str[i] <= "9") {
                        startNumber = i
                    } else {
                        break
                    }
                }
                let repeat = Number(str.slice(startNumber, open))
                let replace = str.slice(open + 1, i).repeat(repeat)
                str = str.slice(0, startNumber) + replace + str.slice(i + 1)
                return dfs(startNumber + replace.length, str, stack)
            }
        }
        result = str
    }
    dfs(0, s, [])
    return result
};