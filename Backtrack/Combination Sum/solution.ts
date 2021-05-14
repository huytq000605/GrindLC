/*
With this question, i use recursion and keep tracking index to dont make same array but different position
*/

function combinationSum(candidates: number[], target: number, current = [], result = [], idx = 0): number[][]|any {
    if(target === 0) return result.push(current)
    for(let i = idx; i < candidates.length; i++) {
        if(candidates[i] <= target) {
            const ori = [...current]
            current.push(candidates[i])
            combinationSum(candidates, target - candidates[i], current, result, i);
            current = ori
        }
    }
    return result
};