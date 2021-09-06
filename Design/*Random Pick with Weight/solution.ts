class Solution {
    w
    constructor(w: number[]) {
        this.w = w
        for(let i = 1; i < w.length; i++) {
            this.w[i] = this.w[i - 1] + this.w[i]
        }
    }

    // The probability to choose is the range of index / total index
    // If we have something like [2,5,3,4] => prefix = [2,7,10,14]
    // If we get [1,2] then return 0
    // If we get [3:7] then return 1
    // If we get [8:10] then return 2
    // If we get [11:14] then return 3
    pickIndex(): number {
        let value = 1 + Math.floor(Math.random() * (this.w[this.w.length - 1] )) // Pass 0
        let min = 1
        let max = this.w.length - 1
        while(min < max) {
            let mid = min + Math.floor((max - min) / 2)
            if(this.w[mid] === value) {
                return mid
            }
            if(this.w[mid] < value) {
                min = mid + 1
            }
            if(this.w[mid] > value) {
                max = mid
            }
        }
        return min
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(w)
 * var param_1 = obj.pickIndex()
 */
