function minimumTime(n: number, relations: number[][], time: number[]): number {
    let finish = Array(n).fill(Number.MAX_SAFE_INTEGER)
    
    let required = new Map()
    for(let relation of relations) {
        if(!required.has(relation[1] - 1)) required.set(relation[1] - 1, [])
        required.get(relation[1] - 1).push(relation[0] - 1)
    }
    
    let learn = (course) => {
        if(finish[course] < Number.MAX_SAFE_INTEGER) return finish[course]
        let timeTake = time[course]
        let timeBonus = 0
        if(required.has(course)) {
            for(let requiredCourse of required.get(course)) {
                timeBonus = Math.max(timeBonus, learn(requiredCourse))
            }
        }
        finish[course] = timeTake + timeBonus
        return timeTake + timeBonus
    }
    
    for(let i = 0; i < n; i++) {
        learn(i)
    }
    
    return Math.max(...finish)
};