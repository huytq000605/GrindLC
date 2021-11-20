function makesquare(matchsticks: number[]): boolean {
    let sum = 0
    for(let s of matchsticks) {
        sum += s
    }
	matchsticks.sort((a,b) => b-a)
    if(sum % 4 !== 0) return false
    let target = sum/4
    let states = Array(4).fill(0)
    let dfs = (index) => {
        if(index >= matchsticks.length) return true
        let seen = new Set()
        for(let i = 0; i < states.length; i++) {
            if(seen.has(states[i])) continue
            if(states[i] + matchsticks[index] <= target) {
                seen.add(states[i])
                states[i] += matchsticks[index]
                if(dfs(index + 1)) return true
                states[i] -= matchsticks[index]
            }
        }
        return false
    }
    
    return dfs(0)
    
};