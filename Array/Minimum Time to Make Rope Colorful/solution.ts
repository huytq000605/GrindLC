function minCost(s: string, cost: number[]): number {
    let result = 0;
    let currentWord = s[0]
    let currentCost = cost[0]
    for(let i = 1; i < s.length; i++) {
        if(s[i] === currentWord) {
            result += Math.min(currentCost, cost[i])
            currentCost = Math.max(currentCost, cost[i])
            continue;
        }
        currentWord = s[i]
        currentCost = cost[i]
    }
    return result
};
