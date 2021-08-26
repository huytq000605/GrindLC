function isValidSerialization(preorder: string): boolean {
    let arr = preorder.split(",")
    let index = 0
    let dfs = () => {
        if(index >= arr.length) return false
        if(arr[index] === "#") {
            return true
        }
        index++
        if(!dfs()) return false
        index++
        if(!dfs()) return false
        
        return true
    }
    if(!dfs()) return false
    if(index !== arr.length - 1) return false
    
    return true
};