function asteroidCollision(asteroids: number[]): number[] {
    let stack = []
    let result = []
    outer:
    for(let asteroid of asteroids) {
        while(asteroid < 0 && result.length && result[result.length - 1] > 0 && -asteroid >= result[result.length - 1]) {
            if(Math.abs(asteroid) === result.pop()) {
                continue outer
            }
        }
        if(asteroid < 0) {
            if(result.length && result[result.length - 1] < 0 || !result.length) result.push(asteroid)
        }
        if(asteroid > 0) {
            result.push(asteroid)
        }
        
    }
    return result
};