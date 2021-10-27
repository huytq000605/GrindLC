function findingUsersActiveMinutes(logs: number[][], k: number): number[] {
    let actionCount = new Map()
    for(let [id, minute] of logs) {
        if(!actionCount.has(id)) actionCount.set(id, new Set())
        actionCount.get(id).add(minute)
    }
    let result = Array(k).fill(0)
    for(let activeMinutesSet of actionCount.values()) {
        result[activeMinutesSet.size - 1]++
    }
    return result
};