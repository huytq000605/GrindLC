function canEat(candiesCount: number[], queries: number[][]): boolean[] {
    let firstCandyType = Array(candiesCount.length + 1).fill(0)
    for(let i = 0; i < firstCandyType.length; i++) {
        if(i > 0) {
            firstCandyType[i] = firstCandyType[i-1]
            firstCandyType[i] += candiesCount[i-1]
        }
    }
    let result = []
    for(let query of queries) {
        let res = true
        let [type, day, cap] = query
        let first = firstCandyType[type] + 1 // first candy of type i
        let perDay = Math.ceil(first / (day + 1))
        if(perDay > cap) {
            res = false
        }
        let last = firstCandyType[type + 1] - 1
        if(last < day) {
            res = false
        }
        result.push(res)
    }
    return result
    
};