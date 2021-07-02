function maxDistance(position: number[], m: number): number {
    position.sort((a,b) => a-b)
    let min = 1
    let max = position[position.length - 1] - position[0] 
    while(min < max) {
        let mid = min + Math.ceil((max-min)/2)
        
        let count = 1
        let currentPosition = position[0]
        for(let i = 1; i < position.length; i++) {
            if(position[i] - currentPosition >= mid) {
                count++
                currentPosition = position[i]
            }
        }
        
        if(count < m) {
            max = mid - 1
         } else {
            min = mid
        }
    }
    return min
};