function maxCompatibilitySum(students: number[][], mentors: number[][]): number {
    let used = new Set()
    
    function helper(index: number) {
        if(index === students.length) {
            return 0
        }
        let result = 0
        for(let j = 0; j < mentors.length; j++) {
                if(used.has(j)) continue
                used.add(j)
                result = Math.max(result, getScore(students[index], mentors[j]) + helper(index + 1))
                used.delete(j)
        }
        return result
    }
    return helper(0)
}


function getScore(s1: number[], s2: number[]) {
    let result = 0
    for(let i = 0; i < s1.length; i++) {
        if(s1[i] === s2[i]) result++
    }
    return result
}