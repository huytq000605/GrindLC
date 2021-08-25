function minElements(nums: number[], limit: number, goal: number): number {
    let sum = 0
    for(let num of nums) {
        sum += num
    }
    let diff = Math.abs(goal - sum)
    return Math.ceil(diff / limit)
};