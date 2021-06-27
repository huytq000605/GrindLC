function stoneGameVI(aliceValues: number[], bobValues: number[]): number {
    let sum = Array(aliceValues.length).fill(0)
    for(let i = 0; i < aliceValues.length; i++) {
        sum[i] = [i, aliceValues[i] + bobValues[i]]
    }
    sum.sort((a,b) => b[1]-a[1])
    let alice = true
    let aPoint = 0
    let bPoint = 0
    for(let i = 0; i < sum.length; i++) {
        if(alice) {
            aPoint += aliceValues[sum[i][0]]
            alice = false
        } else {
            bPoint += bobValues[sum[i][0]]
            alice = true
        }
    }
    if(aPoint > bPoint) return 1
    if(aPoint < bPoint) return -1
    return 0
    
};