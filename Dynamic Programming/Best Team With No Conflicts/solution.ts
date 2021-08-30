function bestTeamScore(scores: number[], ages: number[]): number {
    let teams = Array(scores.length).fill(0).map((e, idx) => [scores[idx], ages[idx]])
    teams.sort((a,b) => b[0] - a[0] || b[1] - a[1])
    let dp = Array(scores.length).fill(0).map(() => Array(1001))
    let dfs = (index: number, minAge: number) => {
        if(index >= scores.length) return 0
        if(dp[index][minAge] !== undefined) return dp[index][minAge]
        let result = dfs(index + 1, minAge) // Pass this person
        if(teams[index][1] <= minAge)
        result = Math.max(result, teams[index][0] + dfs(index + 1, Math.min(teams[index][1], minAge)) )  // Take this person
        dp[index][minAge] = result
        return result
    }
    return dfs(0, 1000)
};