function splitIntoFibonacci(num: string): number[] {
    let arr = []
    let dfs = (idx) => {
        if(idx >= num.length && arr.length >= 3) return true
        if(idx >= num.length) {
            return false
        }
        for(let i = idx; i < num.length; i++) {
            
            let currentNum = Number(num.slice(idx, i + 1))
            if(arr.length < 2 || arr[arr.length - 1] + arr[arr.length - 2] === currentNum && currentNum < Math.pow(2, 31)) {
                arr.push(currentNum)
                if(dfs(i + 1)) return arr
                arr.pop()
            }
            if(num[idx] === "0") break
        }
        
    }
    dfs(0)
    return arr
};