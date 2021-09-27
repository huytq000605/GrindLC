function minSpeedOnTime(dist: number[], hour: number): number {
    if(hour <= dist.length - 1) {
        return -1
    }
    let howLong = (speed) => {
        let totalTime = 0
        for(let i = 0; i < dist.length - 1; i++) {
            totalTime += Math.ceil(dist[i] / speed)
        }
        totalTime += dist[dist.length - 1] / speed
        return totalTime
    }
    let min = 0
    let max = 1e7
    while(min < max) {
        let mid = min + Math.floor((max - min)/ 2)
        let time = howLong(mid)
        if(time > hour) {
            min = mid + 1
        } else {
            max = mid
        }
    }
    return min
};
