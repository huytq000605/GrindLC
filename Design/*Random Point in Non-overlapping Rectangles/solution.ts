class Solution {
    recs
    constructor(rects: any) {
        rects = rects.map((e) => [(e[2] - e[0] + 1) * (e[3] - e[1] + 1), e])
        this.recs = rects
        for(let i = 1; i < this.recs.length; i++) {
            this.recs[i][0] += this.recs[i-1][0]
        }
    }

    pick(): number[] {
        let rand = Math.floor(Math.random() * this.recs[this.recs.length - 1][0]) + 1
        let min = 0
        let max = this.recs.length - 1
        while(min < max) {
            let mid = min + Math.floor((max - min)/2)
            if(this.recs[mid][0] === rand) {
                min = mid
                break
            }
            if(this.recs[mid][0] < rand) {
                min = mid + 1
            } else {
                max = mid
            }
        }
        let rec = this.recs[min][1]
        let u = Math.floor(Math.random() * (rec[2] - rec[0] + 1)) + rec[0]
        let v = Math.floor(Math.random() * (rec[3] - rec[1] + 1)) + rec[1]
        return [u,v]
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(rects)
 * var param_1 = obj.pick()
 */