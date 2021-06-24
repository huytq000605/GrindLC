function combinationSum3(k: number, n: number): number[][] {
    let result = []
    helper(k, n, 0, [], result)
    return result
};

function helper(remaining: number, target: number, maxNumberUsed: number, current: number[], result: number[][]) {
    if(remaining === 0 && target === 0) {
        result.push([...current])
        return
    }
    if(remaining === 0 || target < 0 || maxNumberUsed === 9) {
        return
    }
    current.push(maxNumberUsed + 1)
    helper(remaining - 1, target - maxNumberUsed - 1, maxNumberUsed + 1, current, result)
    current.pop()
    helper(remaining, target, maxNumberUsed + 1, current, result)
    
}