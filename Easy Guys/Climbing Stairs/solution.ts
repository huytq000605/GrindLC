function climbStairs(n: number): number {
    if(n === 1) return 1
    if(n === 2) return 2
    let prev1 = 1
    let prev2 = 2
    for(let i = 3; i <= n; i++) {
        let oriPrev2 = prev2
        prev2 = prev1 + prev2
        prev1 = oriPrev2
    }
    return prev2
};