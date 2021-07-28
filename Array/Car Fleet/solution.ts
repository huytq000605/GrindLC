function carFleet(target: number, position, speed: number[]): number {
    for(let i = 0; i < position.length; i++) {
        position[i] = [position[i], speed[i]]
    }
    let result = 0
    let lastTimeReach = 0
    position.sort((a,b) => b[0]-a[0])
    for(let i = 0; i < position.length; i++) {
        let currentTimeReach = (target - position[i][0])/ position[i][1]
        if(currentTimeReach <= lastTimeReach) continue
        result++
        lastTimeReach = currentTimeReach
    }
    return result
};