class ExamRoom {
    distanceFromLeft
    distanceFromRight
    map
    constructor(n: number) {
        this.distanceFromLeft = Array(n).fill(Number.MAX_SAFE_INTEGER)
        this.distanceFromRight = Array(n).fill(Number.MAX_SAFE_INTEGER)
        this.map = new Map()
    }

    seat(): number {
        let pos = [-1 , 0]
        if(this.map.size === 0) {
            this.map.set(0, true)
            for(let i = 0; i < this.distanceFromLeft.length; i++) {
                this.distanceFromLeft[i] = i
            }
            return 0
        }
        
        for(let i = 0; i < this.distanceFromRight.length; i++) {
            if(this.map.has(i)) continue
            let distance = Math.min(this.distanceFromLeft[i], this.distanceFromRight[i])
            if(distance > pos[1]) {
                pos = [i, distance]
            }
        }
        
        this.map.set(pos[0], true)
        
        for(let i = 0; i < this.distanceFromLeft.length; i++) {
            if(this.map.has(i)) {
                this.distanceFromLeft[i] = 0
            } else {
                if(i === 0) {
                    this.distanceFromLeft[i] = Number.MAX_SAFE_INTEGER
                } else {
                    this.distanceFromLeft[i] = this.distanceFromLeft[i - 1] + 1
                }
            }
        }
        
        for(let i = this.distanceFromRight.length - 1; i >= 0; i--) {
            if(this.map.has(i)) {
                this.distanceFromRight[i] = 0
            } else {
                if(i === this.distanceFromRight.length - 1) {
                    this.distanceFromRight[i] = Number.MAX_SAFE_INTEGER
                } else {
                    this.distanceFromRight[i] = this.distanceFromRight[i + 1] + 1
                }
            }
        }
        
        return pos[0]
        
        
    }

    leave(p: number): void {
        this.map.delete(p)
         for(let i = 0; i < this.distanceFromLeft.length; i++) {
            if(this.map.has(i)) {
                this.distanceFromLeft[i] = 0
            } else {
                if(i === 0) {
                    this.distanceFromLeft[i] = Number.MAX_SAFE_INTEGER
                } else {
                    this.distanceFromLeft[i] = this.distanceFromLeft[i - 1] + 1
                }
            }
        }
        
        for(let i = this.distanceFromRight.length - 1; i >= 0; i--) {
            if(this.map.has(i)) {
                this.distanceFromRight[i] = 0
            } else {
                if(i === this.distanceFromRight.length - 1) {
                    this.distanceFromRight[i] = Number.MAX_SAFE_INTEGER
                } else {
                    this.distanceFromRight[i] = this.distanceFromRight[i + 1] + 1
                }
            }
        }


    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * var obj = new ExamRoom(n)
 * var param_1 = obj.seat()
 * obj.leave(p)
 */