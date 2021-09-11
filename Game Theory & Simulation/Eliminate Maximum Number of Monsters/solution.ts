function eliminateMaximum(dist: number[], speed: number[]): number {
    let reach = Array(dist.length)
    for(let i = 0 ; i < dist.length; i++) {
        reach[i] = Math.ceil(dist[i] / speed[i])
    }
    reach.sort((a,b) => a-b)
    
    for(let i = 0; i < reach.length; i++) {
        let monsterCanBeKill = reach[i]
        if(i + 1 > monsterCanBeKill) {
            return i
        }
    }
    return dist.length
};