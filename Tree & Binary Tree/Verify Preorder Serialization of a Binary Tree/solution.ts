function isValidSerialization(preorder: string): boolean {
    if(preorder === "#") return true
    let node = preorder.split(",")
    let index = 0
    let dfs = () => {
        if(index >= node.length || node[index] === "#") return false
        index++
        if(index >= node.length) {
            return false
        } else if(node[index] !== "#") {
            if(!dfs()) return false
        }
        index++
        if(index >= node.length) {
            return false
        } else if(node[index] !== "#") {
            if(!dfs()) return false
        }
        return true
    }
    if(!dfs()) return false
    if(index !== node.length - 1) return false
    return true
};