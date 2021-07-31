function maxDistToClosest(seats: number[]): number {
    let distance = Array(seats.length).fill(0).map(() => Array(2).fill(100000))
    for(let i = 0; i < seats.length; i++) {
        if(seats[i] === 1) {
            distance[i][0] = 0
        } else {
            if(i === 0) continue
            else distance[i][0] = distance[i - 1][0] + 1
        }
    }
    for(let i = seats.length - 1; i >= 0; i--) {
        if(seats[i] === 1) {
            distance[i][1] = 0
        } else {
            if(i === seats.length - 1) continue
            else distance[i][1] = distance[i+1][1] + 1
        }
    }
    let result = 0
    for(let dist of distance) {
        result = Math.max(result, Math.min(dist[0], dist[1]))
    }
    return result
};