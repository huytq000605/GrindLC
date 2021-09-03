function restoreIpAddresses(s: string): string[] {
    let result = []
    let dfs = (index: number, group: number, current: string) => {
        if(group >= 4) {
            if(index >= s.length) {
                result.push(current.slice(0, current.length - 1))   
                return
            }
            return
            
        }
        if(index >= s.length) {
            return
        }
        dfs(index + 1, group + 1, current + s[index] + ".")
        if(index + 1 <= s.length - 1 && s[index] !== "0") {
            dfs(index + 2, group + 1, current + s[index] + s[index + 1] + ".")
        }
        if(index + 2 <= s.length - 1 && s[index] !== "0" && Number(s.slice(index, index + 3)) <= 255) {
            dfs(index + 3, group + 1, current + s[index] + s[index + 1] + s[index + 2] + ".")
        }
        
    }
    dfs(0, 0, "")
    return result
};