class Robot {
    width
    height
    idx
    DIR
    i
    j
    
    constructor(width: number, height: number) {
        this.width = width
        this.height = height

        this.idx = 0
        this.DIR = [
            ["East", [0, 1]],
            ["North", [1, 0]],
            ["West", [0, -1]],
            ["South", [-1, 0]]
        ]
        this.i = 0
        this.j = 0
    }
    
    out(): boolean {
        if(this.i + this.DIR[this.idx][1][0] < 0 || this.i + this.DIR[this.idx][1][0] >= this.height) return true
        if(this.j + this.DIR[this.idx][1][1] < 0 || this.j + this.DIR[this.idx][1][1] >= this.width) return true
        return false
    }

    move(num: number): void {
        
        while(num > 0) {
            let move
            if(this.DIR[this.idx][1][0] > 0) {
                move = Math.min(num, this.height - this.i - 1)
            } else if(this.DIR[this.idx][1][0] < 0) {
                move = Math.min(num, this.i)
            } else if(this.DIR[this.idx][1][1] > 0) {
                move = Math.min(num, this.width - this.j - 1)
            } else {
                move = Math.min(num, this.j)
            }
            this.i = this.i + this.DIR[this.idx][1][0] * move
            this.j = this.j + this.DIR[this.idx][1][1] * move
            if(move === 0) {
                if(num >= this.width * 2 + this.height * 2 - 4) {
                    num %= (this.width * 2 + this.height * 2 - 4)
                    continue
                }
                
                this.idx = (this.idx + 1) % 4
            }
            num -= move
            
        }
        
        
    }

    getPos(): number[] {
        return [this.j, this.i]
    }

    getDir(): string {
        return this.DIR[this.idx][0]
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * var obj = new Robot(width, height)
 * obj.move(num)
 * var param_2 = obj.getPos()
 * var param_3 = obj.getDir()
 */