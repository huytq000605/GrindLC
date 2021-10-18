function asteroidCollision(asteroids: number[]): number[] {
    let result = []
    outer:
    for(let asteroid of asteroids) {
        while(asteroid < 0 && result.length && result[result.length - 1] > 0 && -asteroid >= result[result.length - 1]) {
            if(-asteroid === result[result.length - 1]) {
                result.pop()
                continue outer
            } else {
                result.pop()
            }
        }
        if(asteroid < 0) {
            // If still remain asteroid > 0 in result, then result[result.length - 1] > current asteroid => skip
            if(result.length && result[result.length - 1] > 0) continue
        }
        result.push(asteroid)
        
    }
    return result
};