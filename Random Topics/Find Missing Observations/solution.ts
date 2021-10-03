function missingRolls(rolls: number[], mean: number, n: number): number[] {
    let m = rolls.length
    let total = mean * (n + m)
    if(total % (m+n) !== 0) return []
    let mTotal = 0
    for(let roll of rolls) mTotal += roll
    let nTotal = total - mTotal
    let eachFloor = Math.floor(nTotal / n)
    let remain = nTotal % n
    if(eachFloor > 6 || eachFloor <= 0) return []
    if(remain > 0 && eachFloor >= 6) return []
    let result = Array(n)
    for(let i = 0; i < n; i++) {
        if(i < remain) result[i] = (eachFloor + 1) 
        else result[i] = eachFloor
    }
    return result
};