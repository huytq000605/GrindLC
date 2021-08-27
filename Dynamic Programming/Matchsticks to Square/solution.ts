function makesquare(matchsticks: number[]): boolean {
    let sum = 0
    for(let s of matchsticks) {
        sum += s
    }
    if(sum % 4 !== 0) return false
    let target = sum/4
    let map = new Map()
    let dfs = (index, arr) => {
        if(index === matchsticks.length) {
            if(arr[0] === arr[1] && arr[1] === arr[2] && arr[2] === arr[3]) 
                return true
            else 
                return false
        }
        let cp = [...arr]
        cp.sort((a,b) => a-b)
        let key = JSON.stringify(cp)
        if(map.has(key)) return false
        for(let i = 0; i < 4; i++) {
            if(cp[i] + matchsticks[index] <= target) {
                cp[i] += matchsticks[index]
                if(dfs(index + 1, cp)) return true
                cp[i] -= matchsticks[index]
            }
        }
        map.set(key, false)
        return false
    }
    return dfs(0, [0,0,0,0])
};