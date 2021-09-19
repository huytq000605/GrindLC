class DetectSquares {
    x
    constructor() {
        this.x = new Map()
    }

    add(point: number[]): void {
        if(!this.x.has(point[0])) this.x.set(point[0], new Map()) // Save by X then Y
        let xMap = this.x.get(point[0])
        xMap.set(point[1], (xMap.get(point[1]) || 0 ) + 1)
    }

    count(point: number[]): number {
        if(!this.x.has(point[0])) {
           return 0
        }
        let freq1 = 1
        let result = 0
        let sameX = this.x.get(point[0]) // get map of same x
        for(let [y, freq2] of sameX.entries()) { // Go through all points
            if(y === point[1]) continue // Same point
            let diff = Math.abs(y - point[1])
            
            let xLeft = point[0] - diff 
            let freq3 = 0
            let freq4 = 0
            if(this.x.has(xLeft)) {
                freq3 = this.x.get(xLeft).get(point[1]) || 0
                freq4 = this.x.get(xLeft).get(y) || 0
            }
            result += freq1 * freq2 * freq3 * freq4
            
            let xRight = point[0] + diff
            freq3 = 0
            freq4 = 0
            if(this.x.has(xRight)) {
                freq3 = this.x.get(xRight).get(point[1]) || 0
                freq4 = this.x.get(xRight).get(y) || 0
            }
            result += freq1 * freq2 * freq3 * freq4
            
        }
        return result
        
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = new DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */