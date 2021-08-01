/*
 * We only need to care about the maximum milestone
 * We call sum as the sum of all milestones except the maximum one
 * If sum < maximum then we just keep pair the maximum with the others, then we put 1 more maximum in the last
 * if sum >= maximum then we know that we can use all the milestones
*/
function numberOfWeeks(milestones: number[]): number {
    let sum = 0
    let max = Number.MIN_SAFE_INTEGER
    for(let m of milestones) {
        sum += m
        max = Math.max(max, m)
    }   
    let sumExceptMax = sum - max
    if(sumExceptMax >= max) {
        return sumExceptMax + max
    } else {
        return sumExceptMax * 2 + 1
    }
}
